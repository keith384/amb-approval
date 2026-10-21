"""Plan requirement: a test asserts every field on each Apple form is covered by the map."""
import json
import sys
from pathlib import Path

from pypdf import PdfReader

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
MAP = json.loads((HERE / "form-field-map.json").read_text())
FORMS = {
    "usecases": REPO / "sources/ma-experience-review/Messages-for-Business_UseCases.pdf",
    "readiness": REPO / "sources/ma-experience-review/Messages-for-Business_Readiness.pdf",
}
EXPECTED = {"usecases": 57, "readiness": 25}

fails = []
for key, pdf in FORMS.items():
    form_fields = set((PdfReader(str(pdf)).get_fields() or {}).keys())
    mapped = {r["field"] for r in MAP[key]}
    missing = form_fields - mapped          # form fields the map doesn't cover
    extra = mapped - form_fields            # map fields not on the form
    if missing:
        fails.append(f"{key}: {len(missing)} form field(s) not in map: {sorted(missing)[:5]}")
    if extra:
        fails.append(f"{key}: {len(extra)} map field(s) not on form: {sorted(extra)[:5]}")
    if len(form_fields) != EXPECTED[key]:
        fails.append(f"{key}: expected {EXPECTED[key]} fields, form has {len(form_fields)}")

if fails:
    print("FAIL:", file=sys.stderr)
    for f in fails:
        print("  -", f, file=sys.stderr)
    sys.exit(1)
print(f"PASS — every Apple form field is covered by the map "
      f"(usecases {EXPECTED['usecases']}, readiness {EXPECTED['readiness']}).")
