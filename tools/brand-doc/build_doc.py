"""
Render the doc model into the Walmart-shape Brand Approval doc (HTML; print to PDF
in a browser) + a readiness note. Runs the terminology lint over the output text
and filename. HTML is the artifact of record (reviewable in Slack); PDF is a
browser/Playwright print step.
"""
from __future__ import annotations
import html
import json
from pathlib import Path

import terminology

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;color:#1b2430;padding:48px;font-size:13.5px;line-height:1.5;max-width:820px;margin:auto}
h1{font-size:26px;font-weight:800;color:#16375c}
.sub{color:#6b7280;margin:4px 0 24px}
h2{font-size:12px;text-transform:uppercase;letter-spacing:.09em;color:#16375c;font-weight:700;margin:22px 0 8px;border-bottom:1px solid #e3e7ec;padding-bottom:4px}
.glance{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:6px}
.glance h3{font-size:11px;text-transform:uppercase;letter-spacing:.06em;color:#9aa4b1;margin-bottom:3px}
table{width:100%;border-collapse:collapse;margin-top:6px;font-size:12.5px}
th{text-align:left;background:#16375c;color:#fff;padding:7px 10px;font-size:10px;text-transform:uppercase;letter-spacing:.05em}
td{padding:7px 10px;border-bottom:1px solid #e8ebef;vertical-align:top}
.bg{display:grid;grid-template-columns:repeat(2,1fr);gap:6px 20px;margin-top:6px}
.bg div{font-size:12.5px}.bg b{color:#16375c}
.ep{font-size:12.5px;color:#374151}
.footer{margin-top:30px;font-size:10px;color:#9aa4b1;border-top:1px solid #eef1f4;padding-top:10px}
@media print{body{padding:24px}}
"""


def _esc(s):
    return html.escape(str(s or ""))


def render_html(model: dict) -> str:
    b = model.get("brand", {})
    n = model.get("narrative", {})
    feats = model.get("features_table", [])
    eps = model.get("entry_points", [])
    rows = "".join(f"<tr><td><b>{_esc(f.get('feature'))}</b></td><td>{_esc(f.get('how_used'))}</td></tr>" for f in feats)
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<title>Apple Messages for Business — Brand Nomination — {_esc(b.get('name'))}</title>
<style>{CSS}</style></head><body>
<h1>Apple Messages for Business — Brand Nomination</h1>
<div class="sub">{_esc(b.get('name'))} &nbsp;·&nbsp; submitted by Linq</div>

<h2>Use Case</h2>
<p>{_esc(n.get('use_case_para'))}</p>

<h2>At a Glance</h2>
<div class="glance">
  <div><h3>The Experience</h3><p>{_esc(n.get('experience'))}</p></div>
  <div><h3>Why It Fits</h3><p>{_esc(n.get('why_it_fits'))}</p></div>
  <div><h3>Value to Users</h3><p>{_esc(n.get('value_to_users'))}</p></div>
  <div><h3>Value to Society</h3><p>{_esc(n.get('value_to_society'))}</p></div>
</div>

<h2>Entry Points</h2>
<div class="ep">{_esc(", ".join(eps)) or "—"}</div>

<h2>Features</h2>
<table><thead><tr><th>Apple feature</th><th>How {_esc(b.get('name'))} would use it</th></tr></thead>
<tbody>{rows or '<tr><td colspan=2>—</td></tr>'}</tbody></table>

<h2>Company Background</h2>
<div class="bg">
  <div><b>Founded:</b> {_esc(b.get('founded')) or '—'}</div>
  <div><b>Headquarters:</b> {_esc(b.get('hq')) or '—'}</div>
  <div><b>Headcount:</b> {_esc(b.get('headcount')) or '—'}</div>
  <div><b>Financials:</b> {_esc(b.get('financials')) or '—'}</div>
</div>

<div class="footer">Linq · Apple Messages for Business brand nomination · HTML artifact (print to PDF)</div>
</body></html>"""


def _open_questions(model: dict) -> list[str]:
    q = []
    b = model.get("brand", {})
    for k in ("requested_date", "define_success", "founded", "hq", "headcount", "financials"):
        if not (b.get(k) or "").strip():
            q.append(f"brand.{k} missing")
    n = model.get("narrative", {})
    for k in ("use_case_para", "experience", "why_it_fits", "value_to_users", "value_to_society"):
        if not (n.get(k) or "").strip():
            q.append(f"narrative.{k} missing")
    for i, uc in enumerate(model.get("use_cases", []), 1):
        if not uc.get("features"):
            q.append(f"use case {i} ({uc.get('title','')}) maps to no enhanced feature — "
                     "state why it isn't text-only")
    return q


def readiness_note(model: dict, lint_hits) -> str:
    oq = _open_questions(model)
    flags = model.get("flags", {})
    out = [f"# Readiness note — {model.get('brand', {}).get('name', '')}", "",
           "_Internal; review before anything goes to Apple._", ""]
    out.append(f"## Open questions ({len(oq)})")
    out += [f"- {x}" for x in oq] or ["- none"]
    out.append("")
    out.append("## Pre-approval / pause flags")
    out += [f"- {x}" for x in (flags.get('pre_approval') or [])] or ["- none"]
    if (flags.get("consumer_ai_pause") or "").strip():
        out.append(f"- consumer-AI pause: {flags['consumer_ai_pause']}")
    out.append("")
    out.append(f"## Terminology lint ({len(lint_hits)})")
    out += [f"- [{h.where}] {h.rule}: \"{h.match}\" → {h.suggestion}" for h in lint_hits] or ["- clean"]
    return "\n".join(out) + "\n"


def build(work_dir: str) -> dict:
    work = Path(work_dir)
    model = json.loads((work / "doc_model.json").read_text())
    brand = (model.get("brand", {}).get("name") or "brand").lower().replace(" ", "-")
    html_doc = render_html(model)

    # lint the rendered prose + filename
    n = model.get("narrative", {})
    lint_text = {**n, "features": " ".join(f.get("how_used", "") for f in model.get("features_table", [])),
                 "filename": f"brand-approval-{brand}"}
    hits = terminology.lint_fields(lint_text)

    (work / f"brand-approval-{brand}.html").write_text(html_doc)
    (work / f"readiness-{brand}.md").write_text(readiness_note(model, hits))
    return {"html": f"brand-approval-{brand}.html", "open_questions": len(_open_questions(model)),
            "terminology_hits": len(hits)}


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(); ap.add_argument("work_dir")
    a = ap.parse_args()
    r = build(a.work_dir)
    print(f"wrote {r['html']} · {r['open_questions']} open questions · {r['terminology_hits']} terminology hits")
