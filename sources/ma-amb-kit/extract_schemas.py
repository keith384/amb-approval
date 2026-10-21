#!/usr/bin/env python3
"""
extract_schemas.py  —  Derive JSON Schema (draft 2020-12) from the AMB canonical.

Reads the *authoritative* line spans + anchors from amb_index.json, slices each
"X Dictionary" table out of AMB_Layer2_Canonical_v7_0.md, and emits one JSON
Schema per dictionary plus a single bundled $defs document.

DESIGN PRINCIPLE — faithfulness over completeness:
  The extractor asserts ONLY what the Apple table states. Where the source is
  ambiguous (empty Type cell, unresolvable "See X" reference, enum-in-prose,
  or an array described in prose but typed 'object'), it emits a faithful,
  permissive node and records the item in schema_coverage_report.md for a human
  to verify — it never invents a concrete type. This keeps the byte-verified
  provenance of the corpus intact.

Outputs (under ./ , i.e. the kit root):
  schemas/<anchor>.json          — 47 self-contained schemas, cross-ref by ./<anchor>.json
  amb_schemas_bundle.json        — all schemas in one $defs doc (#/$defs/<anchor> refs)
  schema_coverage_report.md      — per-schema coverage + everything a human must verify
"""
import json, re, sys, datetime, os
from pathlib import Path
from collections import defaultdict

ROOT   = Path(__file__).resolve().parent
CANON  = Path(os.environ.get("AMB_CANONICAL",
              "/mnt/user-data/uploads/AMB_Layer2_Canonical_v7_0.md"))
_def_index = ROOT / "amb_index.json"
if not _def_index.exists():
    _def_index = Path("/mnt/user-data/uploads/amb_index.json")
INDEX  = Path(os.environ.get("AMB_INDEX", str(_def_index)))
SCHEMA_DIR = ROOT / "schemas"
SCHEMA_DIR.mkdir(exist_ok=True)

DRAFT = "https://json-schema.org/draft/2020-12/schema"
NS    = "https://apple-amb.local/schemas"   # local namespace; not a live URL

# ---- Type vocabulary observed in the canonical dictionary tables ----------
# Maps a normalized Type-cell token -> a JSON Schema type node.
TYPE_MAP = {
    "string":  {"type": "string"},
    "object":  {"type": "object"},
    "array":   {"type": "array"},
    "boolean": {"type": "boolean"},
    "bool":    {"type": "boolean"},
    "integer": {"type": "integer"},
    "int":     {"type": "integer"},
    "number":  {"type": "number"},
    "float":   {"type": "number"},
    "double":  {"type": "number"},
    "byte":    {"type": "string", "contentEncoding": "base64",
                "x-amb-source-type": "byte"},
    "binary":  {"type": "string", "x-amb-source-type": "binary"},
    "dictionary": {"type": "object", "x-amb-source-type": "dictionary"},
    "uuid":    {"type": "string", "format": "uuid",
                "x-amb-source-type": "UUID"},
    "date":    {"type": "string", "x-amb-source-type": "date"},
    "url":     {"type": "string", "format": "uri", "x-amb-source-type": "URL"},
}

def norm_type(t: str) -> str:
    return re.sub(r"[^\w]+$", "", (t or "").strip().lower())

def load_lines():
    return CANON.read_text(encoding="utf-8").split("\n")

def slice_span(lines, a, b):
    # a,b are 1-based inclusive
    return lines[a-1:b]

MD_LINK = re.compile(r"\[([^\]]+)\]\([^)]*\)")

def clean_cell(c: str) -> str:
    c = MD_LINK.sub(r"\1", c)           # [text](url) -> text
    c = re.sub(r"\]\([^)]*\)", "", c)   # residual ](url) from split links
    return c.strip()

NAME_COLS = {"name", "key", "field", "parameter", "property", "attribute"}
TYPE_COLS = {"type"}
DESC_COLS = {"description", "desc", "value", "notes", "meaning"}

def parse_table(span_lines):
    """Return (rows, table_found, layout). Reads the HEADER row to locate the
    name/type/description columns, so 2-column (Name|Description) tables are not
    misread as (Name|Type). Each row is a dict {name, type|None, desc}."""
    rows, header, table_found = [], None, False
    name_i = type_i = desc_i = None
    for ln in span_lines:
        s = ln.strip()
        if s.startswith("|"):
            table_found = True
            cells = [clean_cell(c) for c in s.strip("|").split("|")]
            joined = "".join(cells).replace("-", "").replace(":", "").strip()
            if joined == "":
                continue  # separator row
            if header is None:
                header = [c.lower() for c in cells]
                for i, h in enumerate(header):
                    if name_i is None and h in NAME_COLS: name_i = i
                    elif type_i is None and h in TYPE_COLS: type_i = i
                    elif desc_i is None and h in DESC_COLS: desc_i = i
                # fallbacks when headers are non-standard
                if name_i is None: name_i = 0
                if desc_i is None:
                    desc_i = type_i if (type_i is not None and type_i != name_i) else (len(header) - 1)
                    if type_i == desc_i: type_i = None
                continue
            def cell(i): return cells[i] if (i is not None and i < len(cells)) else ""
            rows.append({
                "name": cell(name_i),
                "type": cell(type_i) if type_i is not None else None,
                "desc": cell(desc_i),
            })
        elif header is not None and s == "":
            if rows: break
        elif header is not None and not s.startswith("|"):
            break
    layout = "3col" if type_i is not None else ("2col" if header else "none")
    return rows, table_found, layout

def find_citation(span_lines):
    for ln in span_lines:
        m = re.search(r"<sub>↳\s*`?([^`<\n]+?)`?\s*</sub>", ln)
        if m:
            return m.group(1).strip()
    return None

def detect_enum_prose(span_lines):
    """Detect 'The possible ... values ... are:' blocks (enum-in-prose)."""
    txt = "\n".join(span_lines)
    m = re.search(r"(possible[^\n]*values[^\n]*(?:are|:))", txt, re.I)
    return m.group(1).strip() if m else None

REQUIRED_RE = re.compile(r"^\s*required\b\.?", re.I)
SEE_RE      = re.compile(r"\bsee\s+([A-Za-z][\w.\-]*)", re.I)
ARRAY_PROSE = re.compile(r"\ban array of\b", re.I)

def rows_to_props(rows, resolve_ref):
    """Convert parsed table rows -> (properties, required, notes) under the
    faithfulness contract. Shared by dictionary schemas and structural object
    schemas so both extract identically. Never invents a type."""
    props, required = {}, []
    notes = {"unresolved_refs": [], "empty_types": [], "unknown_types": [],
             "untyped_prose_fields": [], "array_prose_mismatch": [], "resolved_refs": []}
    for row in rows:
        name_raw, type_raw, desc = row["name"], row["type"], row["desc"]
        toks = name_raw.split()
        field = toks[0] if toks else name_raw
        inline_ref_hint = toks[1] if len(toks) > 1 else None
        t = norm_type(type_raw) if type_raw is not None else None
        is_req = bool(REQUIRED_RE.match(desc))
        see = SEE_RE.search(desc)
        ref_hint = inline_ref_hint or (see.group(1) if see else None)

        node = {}
        if t is None:
            if ref_hint:
                anch, why = resolve_ref(ref_hint)
                if anch:
                    node = {"$ref": f"./{anch}.json"}
                    notes["resolved_refs"].append(f"{field} -> {anch}")
                else:
                    node = {"$comment": "type not specified in source (2-column "
                                        f"Name|Description table); prose ref '{ref_hint}' {why}"}
                    notes["untyped_prose_fields"].append(field)
            else:
                node = {"$comment": "type not specified in source (2-column "
                                    "Name|Description table)"}
                notes["untyped_prose_fields"].append(field)
        elif t in TYPE_MAP:
            node = dict(TYPE_MAP[t])
        elif t == "":
            if ref_hint:
                anch, why = resolve_ref(ref_hint)
                if anch:
                    node = {"$ref": f"./{anch}.json"}
                    notes["resolved_refs"].append(f"{field} -> {anch}")
                else:
                    node = {"$comment": f"references '{ref_hint}' (unresolved in source table)"}
                    notes["unresolved_refs"].append(f"{field}: {why}")
            else:
                node = {"$comment": "type not specified in source table"}
                notes["empty_types"].append(field)
        else:
            node = {"$comment": f"source Type cell = '{type_raw}' (not a known primitive)"}
            notes["unknown_types"].append(f"{field}={type_raw}")

        if t in ("object", "array") and ref_hint:
            anch, why = resolve_ref(ref_hint)
            target = {"$ref": f"./{anch}.json"} if anch else \
                     {"$comment": f"references '{ref_hint}' (unresolved)"}
            if t == "array":
                node["items"] = target
            else:
                if ARRAY_PROSE.search(desc):
                    node.setdefault("x-amb-note",
                        "source prose says 'an array of ...' but Type cell = object")
                    notes["array_prose_mismatch"].append(field)
                node.update(target)
            if not anch:
                notes["unresolved_refs"].append(f"{field}: {why}")
            else:
                notes["resolved_refs"].append(f"{field} -> {anch}")

        if desc:
            node["description"] = desc
        props[field] = node
        if is_req:
            required.append(field)
    return props, required, notes

# ---- A3: explicitly-named STRUCTURAL tables the dictionary heading scan misses.
# Same faithfulness contract; keyed by stable id. object-kind entries become real
# JSON Schemas (and enter the bundle so endpoints can $ref them); matrix/code_table
# entries are emitted as structured reference JSON (not object schemas) under
# structural/ , and are all listed in the coverage report.
STRUCTURAL = [
    {"id": "http-body", "title": "HTTP Body", "kind": "object",
     "line_start": 322, "line_end": 343, "source": "msp-rest-api",
     "note": "The actual /message request body envelope. Interactive messages inherit "
             "from HTTP Body (canonical L419); the interactive path additionally carries "
             "interactiveData (wired in amb.openapi.json to baseinteractivemessage)."},
    {"id": "jwt-claims", "title": "JWT Authorization Fields (JOSE header + claims)",
     "kind": "object", "line_start": 136, "line_end": 145, "source": "msp-rest-api",
     "note": "Subset of JWT fields used to sign the Authorization header; alg is always HS256."},
    {"id": "required-features", "title": "Required Features", "kind": "matrix",
     "line_start": 101, "line_end": 125, "source": "msp-rest-api",
     "note": "Apple's approval matrix (feature x Bot/API x Agent-Triggered). Feeds the "
             "conformance checklist (C2)."},
    {"id": "response-codes", "title": "Response Codes", "kind": "code_table",
     "line_start": 345, "line_end": 398, "source": "msp-rest-api",
     "note": "HTTP response codes returned by /message. Only 5xx are retried (4x, exp backoff)."},
]

def parse_matrix(span_lines):
    """Parse the first pipe-table in a span into (headers, rows-as-lists), preserving
    all columns verbatim. For non-object structural tables (e.g. Required Features)."""
    headers, rows = None, []
    for ln in span_lines:
        s = ln.strip()
        if s.startswith("|"):
            cells = [clean_cell(c) for c in s.strip("|").split("|")]
            joined = "".join(cells).replace("-", "").replace(":", "").strip()
            if joined == "":
                continue
            if headers is None:
                headers = cells
                continue
            rows.append(cells)
        elif headers is not None and s == "" and rows:
            break
        elif headers is not None and not s.startswith("|") and not s.startswith("<sub>"):
            if rows:
                break
    return headers or [], rows

def parse_response_codes(span_lines):
    """Faithfully extract HTTP response codes from the irregular Response Codes
    section (a mix of a header table, prose-rendered 200, and 1-row mini-tables),
    returning [{code, reason, description}]. Descriptions are the source prose."""
    out = []
    i, n = 0, len(span_lines)
    row_re = re.compile(r"^\|\s*(\d{3})\s*\|\s*([^|]+?)\s*\|")
    bare_code = re.compile(r"^\s*(\d{3})\s*$")
    while i < n:
        s = span_lines[i].strip()
        code = reason = None
        j = i + 1
        m = row_re.match(s)
        if m:
            code, reason = m.group(1), m.group(2).strip()
            j = i + 1
        elif bare_code.match(s):  # prose-rendered (e.g. 200 / OK / description)
            code = bare_code.match(s).group(1)
            j = i + 1
            while j < n and span_lines[j].strip() == "":
                j += 1
            reason = span_lines[j].strip() if j < n else ""
            j += 1
        if code:
            desc, k = "", j
            while k < n:
                t = span_lines[k].strip()
                if t == "" or t.startswith("|") or t.startswith("<sub>") \
                        or t.startswith("---") or bare_code.match(t) \
                        or t == "Content-Type: application/json":
                    k += 1
                    continue
                desc = t
                break
            out.append({"code": code, "reason": reason, "description": desc})
        i += 1
    seen, uniq = set(), []
    for r in out:
        if r["code"] in seen:
            continue
        seen.add(r["code"])
        uniq.append(r)
    return uniq

def apply_enrichments(anchor, props, notes, enrich_map, applied_log):
    """Overlay fixture-evidenced types onto typeless fields (C1). Only touches
    fields that are currently untyped ($comment, no type) and only where the
    enrichment carries a confident type. Marks provenance; updates the untyped log."""
    e = enrich_map.get(anchor)
    if not e:
        return
    for field, info in e.items():
        t = info.get("type")
        if not t:
            continue
        node = props.get(field)
        if not node or "type" in node or "$ref" in node:
            continue
        if "$comment" not in node:
            continue
        newnode = {"type": t}
        if node.get("description"):
            newnode["description"] = node["description"]
        newnode["x-amb-enriched-from-fixture"] = {
            "type": t, "observations": info.get("observations"),
            "evidence": info.get("evidence"),
        }
        props[field] = newnode
        if field in notes["untyped_prose_fields"]:
            notes["untyped_prose_fields"].remove(field)
        applied_log.append((anchor, field, t, info.get("observations")))

def main():
    lines = load_lines()
    idx = json.loads(INDEX.read_text(encoding="utf-8"))
    schemas = idx["catalogs"]["schemas"]
    prov_by_key = {p["key"]: p for p in idx["provenance"]}
    enrich_map = {}
    _ep = ROOT / "type_enrichments.json"
    if _ep.exists():
        enrich_map = json.loads(_ep.read_text(encoding="utf-8")).get("enrichments", {})
    applied_enrich = []

    # ---- ref-resolution lookup: candidate label -> {anchors} --------------
    # Keys are lowercased full name AND last dotted segment (both greppable ways
    # Apple writes "See X"). Ambiguous keys (multiple anchors) are left for human.
    label_to_anchors = defaultdict(set)
    for s in schemas:
        name = s["name"]
        for key in {name.lower(), name.split(".")[-1].lower()}:
            label_to_anchors[key].add(s["anchor"])

    def resolve_ref(hint):
        if not hint:
            return None, None
        h = hint.strip().rstrip(".").lower()
        anchors = label_to_anchors.get(h) or label_to_anchors.get(h.split(".")[-1])
        if anchors and len(anchors) == 1:
            return next(iter(anchors)), None
        if anchors and len(anchors) > 1:
            return None, f"ambiguous: '{hint}' -> {sorted(anchors)}"
        return None, f"unresolved: '{hint}'"

    report = []          # per-schema report dicts
    defs = {}            # anchor -> schema node (for bundle)
    per_file = {}        # anchor -> standalone schema (file refs)

    for s in schemas:
        anchor = s["anchor"]
        span = slice_span(lines, s["line_start"], s["line_end"])
        rows, table_found, layout = parse_table(span)
        citation = find_citation(span)
        enum_prose = detect_enum_prose(span)

        props, required, notes = rows_to_props(rows, resolve_ref)
        apply_enrichments(anchor, props, notes, enrich_map, applied_enrich)

        prov = prov_by_key.get(s["source"], {})
        xamb = {
            "anchor": anchor,
            "qualified_name": s.get("qualified_name"),
            "canonical_lines": [s["line_start"], s["line_end"]],
            "source": s["source"],
            "source_rank": prov.get("rank"),
            "source_version": prov.get("version"),
            "source_date": prov.get("date"),
            "source_stale": prov.get("stale", False),
            "source_citation": citation,
            "part": s.get("part"),
            "table_layout": layout,
            "extracted_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        }
        if enum_prose:
            xamb["enum_in_prose_detected"] = enum_prose

        core = {
            "title": s["name"],
            "type": "object",
            "properties": props,
            "additionalProperties": True,   # Apple dicts are open; keep permissive
            "x-amb": xamb,
        }
        if required:
            core["required"] = sorted(set(required))
        if not table_found:
            core["x-amb"]["no_table_in_span"] = True
            core["$comment"] = "No property table in source span; this dictionary " \
                               "is described in prose only. Verify against canonical."

        # standalone file version (own $schema/$id, sibling ./file refs)
        file_schema = {"$schema": DRAFT, "$id": f"{NS}/{anchor}.json", **core}
        per_file[anchor] = file_schema

        # bundle version (defs use #/$defs refs instead of ./file.json)
        bundle_schema = json.loads(
            json.dumps(core).replace(f'"./', f'"#/$defs/').replace(f'.json"', f'"'))
        defs[anchor] = bundle_schema

        report.append({
            "anchor": anchor, "name": s["name"], "source": s["source"],
            "lines": f'{s["line_start"]}-{s["line_end"]}',
            "props": len(props), "required": len(required),
            "table_found": table_found, "layout": layout, "notes": notes,
            "enum_prose": enum_prose,
        })

    dict_schema_count = len(defs)   # 47 dictionary-derived schemas, before structural

    # ---- A3: structural tables -------------------------------------------
    STRUCT_DIR = ROOT / "structural"
    STRUCT_DIR.mkdir(exist_ok=True)
    structural_report = []
    for st in STRUCTURAL:
        span = slice_span(lines, st["line_start"], st["line_end"])
        citation = find_citation(span)
        prov = prov_by_key.get(st["source"], {})
        xamb = {
            "id": st["id"], "structural": True, "kind": st["kind"],
            "canonical_lines": [st["line_start"], st["line_end"]],
            "source": st["source"], "source_rank": prov.get("rank"),
            "source_version": prov.get("version"), "source_date": prov.get("date"),
            "source_stale": prov.get("stale", False), "source_citation": citation,
            "note": st["note"],
            "extracted_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        }
        rec = {"id": st["id"], "title": st["title"], "kind": st["kind"],
               "lines": f'{st["line_start"]}-{st["line_end"]}'}

        if st["kind"] == "object":
            rows, table_found, layout = parse_table(span)
            props, required, notes = rows_to_props(rows, resolve_ref)
            apply_enrichments(st["id"], props, notes, enrich_map, applied_enrich)
            enum_prose = detect_enum_prose(span)
            xamb["table_layout"] = layout
            if enum_prose:
                xamb["enum_in_prose_detected"] = enum_prose
            core = {"title": st["title"], "type": "object", "properties": props,
                    "additionalProperties": True, "x-amb": xamb}
            if required:
                core["required"] = sorted(set(required))
            per_file[st["id"]] = {"$schema": DRAFT, "$id": f"{NS}/{st['id']}.json", **core}
            defs[st["id"]] = json.loads(
                json.dumps(core).replace('"./', '"#/$defs/').replace('.json"', '"'))
            rec.update({"props": len(props), "required": len(required),
                        "notes": notes, "enum_prose": enum_prose})
        elif st["kind"] == "matrix":
            headers, mrows = parse_matrix(span)
            keys = ["feature", "bot_api", "agent_triggered", "description"]
            records = [dict(zip(keys, r + [""] * (len(keys) - len(r)))) for r in mrows]
            doc = {"id": st["id"], "title": st["title"], "x-amb": xamb,
                   "columns": headers, "rows": records}
            (STRUCT_DIR / f"{st['id']}.json").write_text(
                json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
            rec.update({"rows": len(records)})
        elif st["kind"] == "code_table":
            codes = parse_response_codes(span)
            doc = {"id": st["id"], "title": st["title"], "x-amb": xamb, "codes": codes}
            (STRUCT_DIR / f"{st['id']}.json").write_text(
                json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
            rec.update({"rows": len(codes)})
        structural_report.append(rec)

    # ---- build bundle (in memory) ----------------------------------------
    bundle = {
        "$schema": DRAFT,
        "$id": f"{NS}/amb_schemas_bundle.json",
        "title": "Apple Messages for Business — schema bundle (derived from canonical v7.0)",
        "x-amb-generator": {
            "tool": "extract_schemas.py",
            "canonical": idx["meta"]["canonical_file"],
            "canonical_version": idx["meta"]["canonical_version"],
            "generated_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "schema_count": len(defs),
            "dictionary_schema_count": dict_schema_count,
            "structural_object_schema_count": len(defs) - dict_schema_count,
            "faithfulness_note": "Nodes assert only what the source tables state. "
                "Ambiguous items ($comment nodes, x-amb-note) are logged in "
                "schema_coverage_report.md for human verification; none are guessed.",
        },
        "$defs": defs,
    }

    # ---- SELF-VALIDATE before emitting: refuse to write on any failure ----
    from jsonschema import Draft202012Validator
    invalid = []
    for anchor, sch in per_file.items():
        try:
            Draft202012Validator.check_schema(sch)
        except Exception as e:
            invalid.append((anchor, str(e)[:200]))
    try:
        Draft202012Validator.check_schema(bundle)
    except Exception as e:
        invalid.append(("__bundle__", str(e)[:200]))
    if invalid:
        print("ABORT: schema validation failed; nothing written.", file=sys.stderr)
        for a, e in invalid:
            print(f"  {a}: {e}", file=sys.stderr)
        sys.exit(1)

    # ---- write per-file schemas + bundle (validated) ---------------------
    for anchor, sch in per_file.items():
        (SCHEMA_DIR / f"{anchor}.json").write_text(
            json.dumps(sch, ensure_ascii=False, indent=2), encoding="utf-8")
    (ROOT / "amb_schemas_bundle.json").write_text(
        json.dumps(bundle, ensure_ascii=False, indent=2), encoding="utf-8")

    # ---- coverage report --------------------------------------------------
    tot_props = sum(r["props"] for r in report)
    tot_req   = sum(r["required"] for r in report)
    no_table  = [r for r in report if not r["table_found"]]
    unresolved = [(r["anchor"], r["notes"]["unresolved_refs"]) for r in report if r["notes"]["unresolved_refs"]]
    empty     = [(r["anchor"], r["notes"]["empty_types"]) for r in report if r["notes"]["empty_types"]]
    untyped   = [(r["anchor"], r["notes"]["untyped_prose_fields"]) for r in report if r["notes"]["untyped_prose_fields"]]
    unknown   = [(r["anchor"], r["notes"]["unknown_types"]) for r in report if r["notes"]["unknown_types"]]
    arr_mis   = [(r["anchor"], r["notes"]["array_prose_mismatch"]) for r in report if r["notes"]["array_prose_mismatch"]]
    enums     = [(r["anchor"], r["enum_prose"]) for r in report if r["enum_prose"]]

    def block(title, items, fmt):
        if not items:
            return f"### {title}\n\n_None._\n"
        out = f"### {title}\n\n"
        for it in items:
            out += fmt(it) + "\n"
        return out + "\n"

    md = []
    md.append("# AMB Schema Extraction — Coverage Report\n")
    md.append(f"_Generated {datetime.datetime.now(datetime.timezone.utc).isoformat()} "
              f"from `{idx['meta']['canonical_file']}` ({idx['meta']['canonical_version']})._\n")
    md.append("> **Scope.** This covers the 47 `\"Dictionary\"`-headed tables plus the "
              "explicitly-added structural tables (HTTP Body, JWT claims, Required Features, "
              "Response Codes — see the Structural section below). Everything else in the "
              "canonical remains prose and is **not** modelled here: the 47+ dictionaries are "
              "not the complete AMB object model.\n")
    md.append("This report is the honesty layer over the extraction. Every item below is "
              "a place where Apple's source table was silent or ambiguous and the extractor "
              "**declined to guess**. Treat each as a verify-before-relying task.\n")
    md.append("## Totals\n")
    md.append(f"- Dictionary schemas emitted: **{len(report)}**\n"
              f"- Structural tables added (A3): **{len(structural_report)}** "
              f"({sum(1 for r in structural_report if r['kind']=='object')} object schemas, "
              f"{sum(1 for r in structural_report if r['kind']!='object')} data tables)\n"
              f"- Properties extracted (dictionaries): **{tot_props}**\n"
              f"- Required properties (dictionaries): **{tot_req}**\n"
              f"- Schemas with no property table (prose-only): **{len(no_table)}**\n"
              f"- Schemas with unresolved `See X` refs: **{len(unresolved)}**\n"
              f"- Schemas with empty Type cells: **{len(empty)}**\n"
              f"- Schemas using 2-column (Name|Description, no Type) tables: **{len(untyped)}**\n"
              f"- Schemas with non-primitive Type cells: **{len(unknown)}**\n"
              f"- Array-in-prose / object-in-type mismatches: **{len(arr_mis)}**\n"
              f"- Enum-in-prose blocks detected (not auto-encoded): **{len(enums)}**\n"
              f"- Emitted schemas failing draft-2020-12 validation: **{len(invalid)}**\n")

    md.append("\n## Structural tables (A3)\n")
    md.append("| id | title | kind | lines | size |\n|---|---|---|---|---|")
    for r in structural_report:
        size = (f"{r.get('props','?')} props / {r.get('required','?')} req"
                if r["kind"] == "object" else f"{r.get('rows','?')} rows")
        md.append(f"| `{r['id']}` | {r['title']} | {r['kind']} | {r['lines']} | {size} |")
    md.append("\nObject-kind structural schemas (`http-body`, `jwt-claims`) are in the bundle "
              "and `schemas/`; matrix/code tables (`required-features`, `response-codes`) are in "
              "`structural/`. `http-body` is the real `/message` request body (fixes the "
              "previously over-deep mapping).\n")

    md.append("\n## Per-schema coverage\n")
    md.append("| Anchor | Name | Source | Lines | Props | Req | Table |\n|---|---|---|---|---|---|---|")
    for r in report:
        md.append(f"| `{r['anchor']}` | {r['name']} | {r['source']} | {r['lines']} | "
                  f"{r['props']} | {r['required']} | {'yes' if r['table_found'] else 'NO'} |")
    md.append("")

    md.append(block("Prose-only dictionaries (no table to extract)", no_table,
              lambda r: f"- `{r['anchor']}` ({r['name']}, L{r['lines']}) — described in prose; "
                        f"model it by hand from the canonical."))
    md.append(block("Unresolved / ambiguous references", unresolved,
              lambda t: f"- `{t[0]}`: " + "; ".join(t[1])))
    md.append(block("Empty Type cells (left open, not guessed)", empty,
              lambda t: f"- `{t[0]}`: fields {t[1]}"))
    md.append(block("2-column tables — fields with no machine type in source", untyped,
              lambda t: f"- `{t[0]}`: fields {t[1]} (Apple gives description only; "
                        f"assign types by hand or from worked examples)"))
    md.append(block("Fixture-evidenced type enrichments applied (C1)", applied_enrich,
              lambda t: f"- `{t[0]}`.`{t[1]}` -> **{t[2]}** ({t[3]} fixture observations, all agree)"))
    md.append(block("Non-primitive Type cells", unknown,
              lambda t: f"- `{t[0]}`: {t[1]}"))
    md.append(block("Array-in-prose vs object-in-Type mismatches", arr_mis,
              lambda t: f"- `{t[0]}`: fields {t[1]} (kept as source; verify intended shape)"))
    md.append(block("Enum-in-prose detected (encode by hand if desired)", enums,
              lambda t: f"- `{t[0]}`: {t[1]}"))
    if invalid:
        md.append(block("SCHEMAS FAILING VALIDATION (must fix)", invalid,
                  lambda t: f"- `{t[0]}`: {t[1]}"))

    (ROOT / "schema_coverage_report.md").write_text("\n".join(md), encoding="utf-8")

    # ---- console summary --------------------------------------------------
    print(f"dictionary schemas:     {len(report)}")
    print(f"structural tables (A3): {len(structural_report)} "
          f"({', '.join(r['id'] for r in structural_report)})")
    print(f"total object schemas:   {len(per_file)}")
    print(f"properties extracted:   {tot_props}  (required: {tot_req})")
    print(f"prose-only (no table):  {len(no_table)}")
    print(f"unresolved refs:        {len(unresolved)}")
    print(f"2-col untyped fields:   {len(untyped)}")
    print(f"fixture enrichments:    {len(applied_enrich)} applied")
    print(f"non-primitive types:    {len(unknown)}")
    print(f"array/object mismatch:  {len(arr_mis)}")
    print(f"enum-in-prose detected: {len(enums)}")
    print(f"VALIDATION:             all {len(per_file)} object schemas + bundle valid")

if __name__ == "__main__":
    main()
