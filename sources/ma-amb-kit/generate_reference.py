#!/usr/bin/env python3
"""
generate_reference.py — Consolidate all extracted schemas into ONE readable
Markdown reference (reference-only; not a tooling artifact).

Reads amb_schemas_bundle.json (single source of truth for the extracted schemas)
and emits AMB_Schemas_Reference.md: grouped by source/part, each dictionary shown
as a property table with type, required, ref, description, plus its provenance line
span and any faithfulness caveats surfaced inline.
"""
import json, datetime, os, sys
from pathlib import Path
from collections import OrderedDict

ROOT = Path(__file__).resolve().parent
BUNDLE = Path(os.environ.get("AMB_BUNDLE", str(ROOT / "amb_schemas_bundle.json")))

def type_str(node):
    """Compact, human-readable type for a property node."""
    if "$ref" in node:
        target = node["$ref"].split("/")[-1].replace("#", "")
        # bundle refs look like #/$defs/<anchor>
        anchor = node["$ref"].split("/")[-1]
        return f"→ [`{anchor}`](#{anchor})"
    if "$comment" in node and "type" not in node:
        if "2-column" in node["$comment"]:
            return "_(unspecified — 2-col table)_"
        if "unresolved" in node["$comment"] or "references" in node["$comment"]:
            return "_(ref — see note)_"
        return "_(unspecified)_"
    t = node.get("type", "")
    extras = []
    if node.get("format"): extras.append(node["format"])
    if node.get("contentEncoding"): extras.append(node["contentEncoding"])
    if node.get("x-amb-source-type") and node["x-amb-source-type"] not in ("dictionary",):
        extras.append(f'src:{node["x-amb-source-type"]}')
    if node.get("items", {}).get("$ref"):
        extras.append("of " + node["items"]["$ref"].split("/")[-1])
    return t + (f" ({', '.join(extras)})" if extras else "")

def caveat(node, layout=None):
    bits = []
    c = node.get("$comment", "")
    # the generic 2-column note is already conveyed by the schema's header badge;
    # only surface it per-row when it carries extra info (e.g. an unresolved ref)
    if c:
        if layout == "2col" and c.startswith("type not specified in source (2-column") \
                and "ref" not in c:
            pass
        else:
            bits.append(c)
    if "x-amb-note" in node:
        bits.append(node["x-amb-note"])
    return " ".join(bits)

def main():
    if not BUNDLE.exists():
        print(f"ABORT: bundle not found: {BUNDLE}", file=sys.stderr); sys.exit(1)
    b = json.loads(BUNDLE.read_text(encoding="utf-8"))
    defs = b["$defs"]
    if not defs:
        print("ABORT: bundle has no $defs; nothing to render.", file=sys.stderr); sys.exit(1)

    # group by (source, part) preserving first-seen order
    groups = OrderedDict()
    for anchor, sch in defs.items():
        xa = sch.get("x-amb", {})
        key = (xa.get("source", "unknown"), xa.get("part") or "")
        groups.setdefault(key, []).append((anchor, sch))

    n_struct = sum(1 for s in defs.values() if s.get("x-amb", {}).get("structural"))
    n_dict = len(defs) - n_struct
    out = []
    out.append("# Apple Messages for Business — Consolidated Schema Reference\n")
    out.append(f"_Reference only. Generated {datetime.datetime.now(datetime.timezone.utc).isoformat()} "
               f"from `{b['x-amb-generator']['canonical']}` "
               f"({b['x-amb-generator']['canonical_version']}) via the extracted schema bundle._\n")
    out.append(f"> **Scope.** Covers the {n_dict} `\"Dictionary\"`-headed tables plus "
               f"{n_struct} explicitly-added structural object schemas (HTTP Body, JWT claims). "
               "Everything else in the canonical remains prose and is not modelled here — this is "
               "not the complete AMB object model.\n")
    out.append("Each entry asserts only what Apple's source table states; `→` marks a resolved "
               "cross-reference, italic notes mark places the source was silent (see "
               "`schema_coverage_report.md` for the full verify-before-relying list, including the "
               "Required Features and Response Codes tables). For the machine-consumable form, use "
               "`amb_schemas_bundle.json` / `schemas/<anchor>.json`.\n")
    out.append(f"**{len(defs)} object schemas · "
               f"{sum(len(s.get('properties',{})) for s in defs.values())} properties · "
               f"{sum(len(s.get('required',[])) for s in defs.values())} required**\n")


    # table of contents
    out.append("## Contents\n")
    for (source, part), items in groups.items():
        label = f"{source}" + (f" — {part}" if part else "")
        out.append(f"- **{label}**")
        for anchor, sch in items:
            out.append(f"  - [{sch.get('title', anchor)}](#{anchor})")
    out.append("")

    # body
    for (source, part), items in groups.items():
        label = f"{source}" + (f" — {part}" if part else "")
        out.append(f"\n---\n\n## {label}\n")
        for anchor, sch in items:
            xa = sch.get("x-amb", {})
            ls = xa.get("canonical_lines", [None, None])
            out.append(f'<a id="{anchor}"></a>')
            out.append(f"### {sch.get('title', anchor)}\n")
            meta = (f"`{anchor}` · canonical L{ls[0]}–{ls[1]} · source `{xa.get('source')}`"
                    f" (rank {xa.get('source_rank')}, {xa.get('source_date')})"
                    f" · {xa.get('table_layout','?')} table")
            if xa.get("source_citation"):
                meta += f" · ↳ {xa['source_citation']}"
            if xa.get("source_stale"):
                meta += " · ⚠️ STALE source"
            out.append(meta + "\n")

            if sch.get("$comment"):
                out.append(f"> {sch['$comment']}\n")
            if xa.get("enum_in_prose_detected"):
                out.append(f"> **Enum in prose:** {xa['enum_in_prose_detected']}\n")

            props = sch.get("properties", {})
            req = set(sch.get("required", []))
            if props:
                out.append("| Field | Type | Req | Description / note |")
                out.append("|---|---|:---:|---|")
                for fld, node in props.items():
                    desc = node.get("description", "").replace("\n", " ").strip()
                    cv = caveat(node, xa.get("table_layout"))
                    # if the only description is the caveat-bearing $comment, show desc; append note
                    cell = desc
                    if cv and cv not in desc:
                        cell = (desc + ("<br>_" + cv + "_" if desc else "_" + cv + "_"))
                    cell = cell.replace("|", "\\|")
                    r = "✓" if fld in req else ""
                    out.append(f"| `{fld}` | {type_str(node)} | {r} | {cell} |")
                out.append("")
            else:
                out.append("_No property table in source (prose-only dictionary)._\n")

    md = "\n".join(out)
    (ROOT / "AMB_Schemas_Reference.md").write_text(md, encoding="utf-8")
    print(f"schemas: {len(defs)} | groups: {len(groups)} | bytes: {len(md)}")

if __name__ == "__main__":
    main()
