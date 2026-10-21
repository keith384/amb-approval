"""
Fill Apple's two Messages-for-Business AcroForms (Use Cases, Readiness) from a
scope.json using the extracted field map (form-field-map.json). Field names are
Apple's exact (misspellings and all); the map's `maps_to` dotted keys resolve
against the scope. Reports coverage (filled / blank = open question) and runs the
terminology lint over text values. No field is invented.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter

import terminology

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
MAP = json.loads((HERE / "form-field-map.json").read_text())
FORMS = {
    "usecases": REPO / "sources/ma-experience-review/Messages-for-Business_UseCases.pdf",
    "readiness": REPO / "sources/ma-experience-review/Messages-for-Business_Readiness.pdf",
}


def _resolve(scope: dict, dotted: str):
    cur = scope
    for part in (dotted or "").split("."):
        if isinstance(cur, dict) and part in cur:
            cur = cur[part]
        else:
            return None
    return cur


def _field_value(spec: dict, raw):
    """Coerce a scope value to what pypdf wants for this field type."""
    if raw is None:
        return None
    t = spec["type"]
    if t == "text":
        return str(raw)
    if t == "checkbox":
        on = next((o for o in (spec.get("options") or ["On"]) if o.lower() != "off"), "On")
        return on if raw in (True, "true", "True", 1, "yes", "Yes", "on", "On") else None
    if t == "radio":
        opts = spec.get("options") or []
        # accept exact option match (case-insensitive)
        for o in opts:
            if str(raw).strip().lower() == o.lower():
                return o
        return None
    return str(raw)


def fill(form_key: str, scope: dict, out_path: Path) -> dict:
    reader = PdfReader(str(FORMS[form_key]))
    writer = PdfWriter()
    writer.append(reader)
    try:
        writer.set_need_appearances_writer(True)
    except Exception:
        pass

    values, blanks, text_vals = {}, [], {}
    for spec in MAP[form_key]:
        raw = _resolve(scope, spec.get("maps_to") or "")
        v = _field_value(spec, raw)
        if v is None:
            blanks.append(spec["field"])
        else:
            values[spec["field"]] = v
            if spec["type"] == "text":
                text_vals[spec["field"]] = v

    for page in writer.pages:
        try:
            writer.update_page_form_field_values(page, values, auto_regenerate=False)
        except Exception:
            pass

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("wb") as fh:
        writer.write(fh)

    lint = terminology.lint_fields(text_vals)
    return {"form": form_key, "total_fields": len(MAP[form_key]),
            "filled": len(values), "blank_open_questions": blanks,
            "terminology_hits": [vars(h) for h in lint], "out": str(out_path)}


def fill_all(scope_path: str, out_dir: str) -> dict:
    scope = json.loads(Path(scope_path).read_text())
    b = scope.get("brand")
    brand = ((b.get("name") if isinstance(b, dict) else b) or "brand").lower().replace(" ", "-")
    out = Path(out_dir)
    res = {}
    for key in FORMS:
        res[key] = fill(key, scope, out / f"{brand}-{key}.pdf")
    return res


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("scope"); ap.add_argument("out_dir")
    a = ap.parse_args()
    r = fill_all(a.scope, a.out_dir)
    for key, info in r.items():
        print(f"{key}: filled {info['filled']}/{info['total_fields']} "
              f"({len(info['blank_open_questions'])} open) → {Path(info['out']).name}")
        if info["terminology_hits"]:
            print(f"  ⚠ terminology: {len(info['terminology_hits'])} hit(s)")
            for h in info["terminology_hits"][:5]:
                print(f"    [{h['where']}] {h['rule']}: {h['match']!r} → {h['suggestion']}")
