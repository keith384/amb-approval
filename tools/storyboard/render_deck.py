"""
Render the storyboard slide model (brand review → generate.py) into the Linq/Juno
submission deck: a cover + one landscape slide per section, each a row of step
columns. Each step shows "STEP n · USER DOES/PAGE DISPLAYS", a tag pill (Apple
feature = purple), a one-line description, and an iMessage screen. HTML (print to PDF).
"""
from __future__ import annotations
import html

def _esc(s):
    return html.escape(str(s or ""))

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:#eef1f4;color:#1b2430;padding:28px}
.slide{background:#fff;border-radius:14px;box-shadow:0 2px 10px rgba(0,0,0,.08);padding:30px 34px;margin:0 auto 24px;max-width:1280px}
.cover h1{font-size:30px;font-weight:800;color:#16375c}
.cover .sub{color:#6b7280;margin:6px 0 16px;font-size:14px}
.cover .fmt{background:#f6f8fa;border:1px solid #e3e7ec;border-radius:10px;padding:14px 16px;font-size:13px;color:#374151;line-height:1.5;margin-bottom:14px}
.uclist{display:flex;gap:10px;flex-wrap:wrap}
.uccard{border:1px solid #e3e7ec;border-radius:10px;padding:10px 12px;min-width:200px}
.uccard b{color:#16375c;font-size:13px}
h2{font-size:19px;font-weight:800;color:#16375c}
.desc{color:#55606e;font-size:13px;margin:4px 0 16px;max-width:900px;line-height:1.45}
.steps{display:flex;gap:16px;overflow-x:auto;padding-bottom:6px}
.step{width:220px;flex:0 0 220px}
.stephead{font-size:10px;font-weight:700;letter-spacing:.05em;color:#8a929c;text-transform:uppercase}
.tag{display:inline-block;font-size:10px;font-weight:700;border-radius:5px;padding:1px 6px;margin:5px 0}
.tag.feature{background:#efe7fb;color:#6b3fd1;border:1px solid #d9c7f4}
.tag.req{background:#fdeeea;color:#b4521e;border:1px solid #f3cdbd}
.tag.entry{background:#e7f1fb;color:#2f6db0;border:1px solid #c6ddf2}
.stepdesc{font-size:11.5px;color:#374151;margin:4px 0 9px;line-height:1.4;min-height:42px}
.phone{background:#fff;border:7px solid #111;border-radius:28px;height:380px;overflow:hidden;position:relative}
.nav{text-align:center;font-size:10px;color:#8a929c;padding:6px 0 7px;border-bottom:1px solid #eee}
.nav b{display:block;color:#111;font-size:11px}
.scr{padding:8px;display:flex;flex-direction:column;gap:5px;overflow:hidden}
.b{max-width:82%;padding:6px 9px;border-radius:14px;font-size:11px;line-height:1.35}
.bot{align-self:flex-start;background:#e9e9eb;color:#111;border-bottom-left-radius:4px}
.user{align-self:flex-end;background:#2f7bf6;color:#fff;border-bottom-right-radius:4px}
.chips{display:flex;flex-wrap:wrap;gap:4px;align-self:flex-start;max-width:92%}
.chip{border:1px solid #2f7bf6;color:#2f7bf6;border-radius:13px;padding:3px 8px;font-size:10px}
.card{align-self:flex-start;width:92%;border:1px solid #e3e7ec;border-radius:11px;padding:8px;font-size:10.5px}
.card .k{font-size:8.5px;text-transform:uppercase;letter-spacing:.06em;color:#9aa4b1;margin-bottom:3px}
@media print{body{background:#fff}.slide{box-shadow:none;break-inside:avoid;page-break-after:always}}
"""

ELEMENT_LABEL = {"list_picker": "List Picker", "time_picker": "Time Picker", "rich_link": "Rich Link",
                 "apple_pay": "Apple Pay", "auth": "Authentication"}


def _screen(scr: dict) -> str:
    if not scr:
        return '<div class="phone"></div>'
    parts = []
    for bub in scr.get("bubbles", []) or []:
        side = "user" if bub.get("side") == "user" else "bot"
        parts.append(f'<div class="b {side}">{_esc(bub.get("text"))}</div>')
    chips = scr.get("chips") or []
    if chips:
        parts.append('<div class="chips">' + "".join(f'<span class="chip">{_esc(c)}</span>' for c in chips) + "</div>")
    el = scr.get("element")
    if el and el != "none" and el in ELEMENT_LABEL and el not in ("quick_reply",):
        parts.append(f'<div class="card"><div class="k">{ELEMENT_LABEL[el]}</div></div>')
    return (f'<div class="phone"><div class="nav"><b>{_esc(scr.get("nav"))}</b>Apple Messages for Business</div>'
            f'<div class="scr">{"".join(parts)}</div></div>')


def _tag(tag: dict) -> str:
    if not tag or not tag.get("text"):
        return ""
    t = (tag.get("type") or "").lower()
    cls = "feature" if "feature" in t else "req" if "require" in t else "entry" if "entry" in t else "feature"
    return f'<span class="tag {cls}">{_esc(tag.get("type"))}: {_esc(tag.get("text"))}</span>'


def _step(i: int, step: dict) -> str:
    return (f'<div class="step"><div class="stephead">STEP {i} · {_esc(step.get("mode", "USER DOES"))}</div>'
            f'{_tag(step.get("tag") or {})}'
            f'<div class="stepdesc">{_esc(step.get("description"))}</div>'
            f'{_screen(step.get("screen") or {})}</div>')


def render_html(model: dict) -> str:
    brand = model.get("brand", "Brand")
    cover = model.get("cover") or {}
    uc = cover.get("use_cases") or []
    uc_html = "".join(
        f'<div class="uccard"><b>{_esc(u.get("title"))}</b><div style="margin-top:4px">'
        + "".join(f'<span class="tag feature">{_esc(f)}</span> ' for f in (u.get("features") or []))
        + "</div></div>" for u in uc)
    out = [f'<!DOCTYPE html><html><head><meta charset="utf-8"><title>Storyboard — {_esc(brand)}</title>',
           f"<style>{CSS}</style></head><body>",
           f'<div class="slide cover"><h1>{_esc(brand)} × Apple Messages for Business</h1>',
           '<div class="sub">Experience flows for the Linq / Apple submission · draft</div>',
           '<div class="fmt">Format: describe the use case → "User does…" + screen → "Page displays…" + '
           'screen → repeat until the use case is complete. Matches the submitted use-case doc; purple tags '
           'are the Apple features selected per use case.</div>',
           (f'<div style="margin:8px 0 4px;color:#55606e;font-size:13px">{_esc(cover.get("summary"))}</div>' if cover.get("summary") else ""),
           f'<div class="uclist">{uc_html}</div></div>']
    for s in model.get("sections", []):
        steps = "".join(_step(i + 1, st) for i, st in enumerate(s.get("steps", [])))
        out.append(f'<div class="slide"><h2>{_esc(s.get("title"))}</h2>'
                   f'<div class="desc">{_esc(s.get("description"))}</div>'
                   f'<div class="steps">{steps}</div></div>')
    out.append("</body></html>")
    return "\n".join(out)
