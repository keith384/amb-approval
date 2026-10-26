"""
Build a Tool 1 intake from a brand's own source documents (the PDFs an AE drops in
Slack: brand nomination, Apple Use Cases form, etc.). Extracts the PDF text and has
Claude synthesize the structured intake (brand facts + 4 use cases + entry points +
company background) that brand_doc.py consumes. Uses ONLY facts in the sources.

    python intake_from_sources.py "<Brand>" <out_intake.json> <file1.pdf> [file2.pdf ...] [--note "..."]
"""
from __future__ import annotations
import json
import os
import re
import sys
from pathlib import Path

from pypdf import PdfReader

MODEL = os.environ.get("AMB_LLM_MODEL", "claude-opus-4-8")


def extract_text(paths: list[str], cap: int = 60000) -> str:
    chunks = []
    for p in paths:
        try:
            txt = "".join((pg.extract_text() or "") for pg in PdfReader(p).pages)
        except Exception as e:
            txt = f"(could not read: {e})"
        chunks.append(f"=== {Path(p).name} ===\n{txt}")
    return "\n\n".join(chunks)[:cap]


def run(brand: str, paths: list[str], note: str = "") -> dict:
    import anthropic
    text = extract_text(paths)
    system = (
        "You build a structured intake for an Apple Messages for Business brand-approval "
        "submission from the brand's OWN source documents. Output STRICT JSON only, matching:\n"
        '{"brand":{"name":"","requested_date":"","website":"","app":"","support_hours":"",'
        '"existing_agent":"","define_success":""},'
        '"use_cases":["4 one-sentence use cases in the customer\'s voice"],'
        '"entry_points":["subset of app_messages_button|web_messages_button|qr_code|message_suggest|ivr_deflect|apple_maps|social_media"],'
        '"company_background":{"founded":"","hq":"","headcount":"","financials":""}}\n'
        "Use ONLY facts present in the sources; leave unknown fields as empty strings. Never "
        'invent features, metrics, or claims. Never use "iMessage"/"AMB"/"Apple Chat".')
    user = f"BRAND: {brand}\n" + (f"NOTE FROM THE AE: {note}\n" if note else "") + \
           f"\nSOURCE DOCUMENTS:\n{text}\n\nProduce the intake JSON."
    client = anthropic.Anthropic()
    resp = client.messages.create(model=MODEL, max_tokens=4000, system=system,
                                  messages=[{"role": "user", "content": user}])
    m = re.search(r"\{.*\}", resp.content[0].text, re.S)
    intake = json.loads(m.group(0)) if m else {"brand": {"name": brand}}
    intake.setdefault("brand", {})["name"] = brand  # authoritative
    return intake


if __name__ == "__main__":
    args = sys.argv[1:]
    note = ""
    if "--note" in args:
        i = args.index("--note"); note = args[i + 1]; args = args[:i] + args[i + 2:]
    brand, out, pdfs = args[0], args[1], args[2:]
    intake = run(brand, pdfs, note)
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    Path(out).write_text(json.dumps(intake, indent=2))
    uc = intake.get("use_cases", [])
    print(f"intake for {brand}: {len(uc)} use cases, entry_points {intake.get('entry_points')} → {out}")
