#!/usr/bin/env python3
"""
extract_fixtures.py — C1. Extract worked JSON payloads from the code-example
sections into per-message-type fixtures, and derive fixture-evidenced type
enrichments for the typeless 2-column fields.

Faithfulness: Apple's examples are illustrative, not literal JSON — they carry
unquoted placeholders (HS256, <destinationId>) and stray tokens. This tool does a
MINIMAL, LOGGED, reversible normalization that fixes only placeholder *syntax*
(wrapping bare/angle-bracket tokens as JSON strings); it never invents field values.
Type evidence is drawn ONLY from genuine literals, never from a substituted token.
Anything still unparseable is stored verbatim under fixtures/_unparsed/ for humans.

Outputs:
  fixtures/<group>/<slug>.json     — normalized, valid payloads
  fixtures/_unparsed/<slug>.txt    — raw blocks that couldn't be made valid
  fixtures/manifest.json           — provenance + normalization log per fixture
  type_enrichments.json            — fixture-evidenced types for typeless fields
  fixtures_report.md               — human summary
"""
import json, re, os, datetime
from pathlib import Path
from collections import defaultdict

ROOT  = Path(__file__).resolve().parent
CANON = Path(os.environ.get("AMB_CANONICAL",
             "/mnt/user-data/uploads/AMB_Layer2_Canonical_v7_0.md"))
_def_index = ROOT / "amb_index.json"
if not _def_index.exists():
    _def_index = Path("/mnt/user-data/uploads/amb_index.json")
INDEX = Path(os.environ.get("AMB_INDEX", str(_def_index)))
FIX_DIR = ROOT / "fixtures"

def slugify(s):
    s = re.sub(r"[^A-Za-z0-9]+", "-", s.strip().lower()).strip("-")
    return s or "block"

# section-title -> fixture group
def group_for(title):
    t = title.lower()
    if "text message" in t: return "text"
    if "form message" in t or "form" == t: return "form"
    if "authenticat" in t: return "authentication"
    if "closesession" in t or "close" in t: return "close-session"
    if "payment method" in t: return "apple-pay"
    if "payment" in t or "apple pay" in t: return "apple-pay"
    if "replymessage" in t: return "interactive-common"
    if "imageitem" in t: return "interactive-common"
    if "quick reply" in t: return "quick-reply"
    if "list picker" in t: return "list-picker"
    if "time picker" in t: return "time-picker"
    if "tutorial" in t or "msp-api-tutorial" in t: return "tutorial"
    if "msp-rest-api" in t: return "rest-api-reference"
    if "merchant token" in t or "decrypt" in t or "payment sheet" in t or "payment object" in t:
        return "apple-pay"
    return "misc"

def find_json_core(text):
    """Return the first balanced {...}/[...] substring, respecting strings/escapes."""
    start = None
    for i, ch in enumerate(text):
        if ch in "{[":
            start = i; break
    if start is None:
        return None
    depth = 0; in_str = False; esc = False
    for j in range(start, len(text)):
        ch = text[j]
        if in_str:
            if esc: esc = False
            elif ch == "\\": esc = True
            elif ch == '"': in_str = False
        else:
            if ch == '"': in_str = True
            elif ch in "{[": depth += 1
            elif ch in "}]":
                depth -= 1
                if depth == 0:
                    return text[start:j + 1]
    return None

def normalize(core):
    """Fix placeholder SYNTAX only. Returns (normalized, substitutions[])."""
    subs = []
    # 1) angle-bracket placeholders used as a value:  : <foo>  ->  : "<foo>"
    def ph(m):
        subs.append({"kind": "angle", "token": m.group(2)})
        return f'{m.group(1)}"{m.group(2)}"{m.group(3)}'
    out = re.sub(r'(:\s*)(<[^>\n]+>)(\s*[,}\]\n])', ph, core)
    # 2) bare identifier used as a value:  : HS256  ->  : "HS256"
    def bare(m):
        tok = m.group(2)
        if tok in ("true", "false", "null"):
            return m.group(0)
        subs.append({"kind": "bare", "token": tok})
        return f'{m.group(1)}"{tok}"{m.group(3)}'
    out = re.sub(r'(:\s*)([A-Za-z_][A-Za-z0-9_\-\.]*)(\s*[,}\]\n])', bare, out)
    return out, subs

def literal_type(v):
    if isinstance(v, bool): return "boolean"
    if isinstance(v, int): return "integer"
    if isinstance(v, float): return "number"
    if isinstance(v, str): return "string"
    if isinstance(v, list): return "array"
    if isinstance(v, dict): return "object"
    return None

# schema-anchor -> (payload parent-key, [typeless fields]) for evidence gathering
def enrichment_targets(idx_report):
    # read coverage-derived typeless targets straight from the bundle x-amb notes is
    # overkill; hardcode the mapping from schema anchor to the JSON parent key.
    return {
        "replymessage-dictionary": ("replyMessage",
            ["title", "subtitle", "imageTitle", "imageSubtitle",
             "secondarySubtitle", "tertiarySubtitle", "imageIdentifier", "style"]),
        "payment-method-dictionary": ("paymentMethod", ["type"]),
        "payment-dictionary":   ("payment", ["billingContact", "paymentToken", "shippingContact"]),
        "payment-dictionary-1": ("payment", ["shippingContact"]),
        "payment-dictionary-2": ("payment", ["paymentMethod"]),
        "payment-dictionary-3": ("payment", ["shippingMethod"]),
        "payment-dictionary-4": ("payment",
            ["billingContact", "errors", "shippingContact", "shippingMethod", "summaryItems"]),
    }

def walk_collect(obj, parent_key, subbed_tokens, evidence, targets_by_parent):
    """Recursively collect (parent_key,field)->json-type from GENUINE literals."""
    if isinstance(obj, dict):
        fields = targets_by_parent.get(parent_key)
        for k, v in obj.items():
            if fields and k in fields:
                # skip if this value came from a placeholder substitution
                if isinstance(v, str) and v in subbed_tokens:
                    continue
                t = literal_type(v)
                if t:
                    evidence[(parent_key, k)].append(t)
            walk_collect(v, k, subbed_tokens, evidence, targets_by_parent)
    elif isinstance(obj, list):
        for it in obj:
            walk_collect(it, parent_key, subbed_tokens, evidence, targets_by_parent)

def main():
    lines = CANON.read_text(encoding="utf-8").split("\n")
    idx = json.loads(INDEX.read_text(encoding="utf-8"))
    ces = idx["catalogs"]["code_examples"]

    if FIX_DIR.exists():
        for p in FIX_DIR.rglob("*"):
            if p.is_file(): p.unlink()
    (FIX_DIR / "_unparsed").mkdir(parents=True, exist_ok=True)

    targets = enrichment_targets(idx)
    targets_by_parent = defaultdict(dict)
    for anchor, (pkey, flds) in targets.items():
        for f in flds:
            targets_by_parent[pkey][f] = anchor
    # collapse to parent->set(fields)
    tbp = {pk: set(d.keys()) for pk, d in targets_by_parent.items()}

    manifest = []
    evidence = defaultdict(list)   # (parent_key, field) -> [types]
    counts = defaultdict(int)
    n_valid = n_unparsed = 0

    for c in ces:
        span = "\n".join(lines[c["line_start"] - 1:c["line_end"]])
        blocks = list(re.finditer(r"```json\s*(.*?)```", span, re.S))
        group = group_for(c["title"])
        for bi, m in enumerate(blocks):
            raw = m.group(1)
            core = find_json_core(raw)
            slug = f'{slugify(c["title"])}-{c["line_start"]}-{bi}'
            if core is None:
                (FIX_DIR / "_unparsed" / f"{slug}.txt").write_text(raw.strip(), encoding="utf-8")
                manifest.append({"slug": slug, "group": group, "section": c["title"],
                                 "line": c["line_start"], "block": bi,
                                 "status": "no-json-core"})
                n_unparsed += 1
                continue
            norm, subs = normalize(core)
            try:
                obj = json.loads(norm)
            except Exception as e:
                (FIX_DIR / "_unparsed" / f"{slug}.txt").write_text(raw.strip(), encoding="utf-8")
                manifest.append({"slug": slug, "group": group, "section": c["title"],
                                 "line": c["line_start"], "block": bi,
                                 "status": "unparsed", "error": str(e)[:120]})
                n_unparsed += 1
                continue
            gdir = FIX_DIR / group
            gdir.mkdir(exist_ok=True)
            (gdir / f"{slug}.json").write_text(
                json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")
            counts[group] += 1
            n_valid += 1
            subbed_tokens = {s["token"] for s in subs}
            walk_collect(obj, None, subbed_tokens, evidence, tbp)
            manifest.append({
                "slug": slug, "group": group, "section": c["title"],
                "canonical_line": c["line_start"], "block": bi,
                "status": "ok", "normalized": bool(subs),
                "substitutions": subs,
                "top_level_keys": sorted(obj.keys()) if isinstance(obj, dict) else None,
            })

    # ---- fixture-evidenced type enrichments ------------------------------
    enrichments = {}
    parent_to_anchor = {pk: {f: a for a, (p, fs) in targets.items() if p == pk for f in fs}
                        for pk in {p for _, (p, _) in targets.items()}}
    for (pkey, field), types in evidence.items():
        uniq = sorted(set(types))
        anchor = None
        for a, (p, fs) in targets.items():
            if p == pkey and field in fs:
                anchor = a; break
        if not anchor:
            continue
        if len(uniq) == 1:
            enrichments.setdefault(anchor, {})[field] = {
                "type": uniq[0], "observations": len(types),
                "evidence": "fixture literals (all agree)",
            }
        else:
            enrichments.setdefault(anchor, {})[field] = {
                "type": None, "observations": len(types),
                "conflict": uniq, "evidence": "fixtures disagree — left typeless",
            }
    (ROOT / "type_enrichments.json").write_text(
        json.dumps({"generated_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                    "note": "Types inferred ONLY from genuine fixture literals; conflicts left null. "
                            "Applied by extract_schemas.py as x-amb-enriched-from-fixture.",
                    "enrichments": enrichments}, ensure_ascii=False, indent=2), encoding="utf-8")

    (FIX_DIR / "manifest.json").write_text(
        json.dumps({"generated_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                    "canonical": CANON.name, "valid": n_valid, "unparsed": n_unparsed,
                    "by_group": dict(counts), "fixtures": manifest},
                   ensure_ascii=False, indent=2), encoding="utf-8")

    # ---- report ----------------------------------------------------------
    md = ["# AMB Fixtures — Extraction Report\n",
          f"_Generated {datetime.datetime.now(datetime.timezone.utc).isoformat()} from `{CANON.name}`._\n",
          "Worked payloads extracted from the code-example sections. Apple's examples are "
          "illustrative JSON with placeholders; normalization fixes only placeholder **syntax** "
          "(logged per fixture in `manifest.json`), never field values. Type evidence is taken "
          "only from genuine literals.\n",
          f"- Valid fixtures: **{n_valid}**  ·  Unparsed (kept raw): **{n_unparsed}**\n",
          "## By group\n"]
    for g, n in sorted(counts.items()):
        md.append(f"- `{g}`: {n}")
    md.append("\n## Fixture-evidenced type enrichments\n")
    if enrichments:
        md.append("| Schema | Field | Inferred type | Observations |\n|---|---|---|---|")
        for a, flds in enrichments.items():
            for f, info in flds.items():
                t = info["type"] or f"conflict {info.get('conflict')}"
                md.append(f"| `{a}` | `{f}` | {t} | {info['observations']} |")
    else:
        md.append("_No enrichments derived._")
    md.append("\nEnrichments are applied to the schemas by `extract_schemas.py` (marked "
              "`x-amb-enriched-from-fixture`) and re-listed in `schema_coverage_report.md`.")
    (ROOT / "fixtures_report.md").write_text("\n".join(md), encoding="utf-8")

    print(f"valid fixtures:   {n_valid}")
    print(f"unparsed (raw):   {n_unparsed}")
    print(f"groups:           {dict(counts)}")
    print(f"enrichments:      {sum(len(v) for v in enrichments.values())} fields across "
          f"{len(enrichments)} schemas")
    for a, flds in enrichments.items():
        for f, info in flds.items():
            print(f"   {a}.{f} -> {info['type'] or info.get('conflict')} ({info['observations']} obs)")

if __name__ == "__main__":
    main()
