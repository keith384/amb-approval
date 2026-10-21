"""
Render an authored flow into the storyboard: one annotated iPhone frame per step,
laid out as Flow A / B / C, as HTML (browser print-to-PDF). Each frame draws the
step's element to an approximation of Apple's layout and is captioned with the
step number, actor, and the checklist Refs it evidences.
"""
from __future__ import annotations
import html

# step kind → checklist Refs the step is expected to evidence (for the shot list).
KIND_REFS = {
    "framing": ["4.5"], "text": ["3.1"], "quick_reply": ["5.4"], "list_picker": ["5.4", "LP1"],
    "time_picker": ["5.12", "TP1"], "rich_link": ["4.1", "RL1"], "apple_pay": ["7.1", "AP1"],
    "auth": ["7.1", "AU1"], "handoff": ["9.1", "G3"],
}


def refs_for(step: dict) -> list[str]:
    k = step["kind"]
    if step.get("actor") == "human":
        return KIND_REFS["handoff"]
    return KIND_REFS.get(k, [])


def _esc(s):
    return html.escape(str(s or ""))


CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;background:#f4f6f8;color:#1b2430;padding:40px}
h1{font-size:24px;font-weight:800;color:#16375c}
.sub{color:#6b7280;margin:4px 0 20px}
h2{font-size:14px;color:#16375c;margin:26px 0 10px}
.flow{display:flex;gap:18px;flex-wrap:wrap}
.cell{width:230px}
.phone{width:230px;height:420px;background:#fff;border:8px solid #111;border-radius:34px;padding:10px 10px 0;overflow:hidden;position:relative;box-shadow:0 6px 18px rgba(0,0,0,.12)}
.nav{text-align:center;font-size:11px;color:#8a929c;border-bottom:1px solid #eee;padding-bottom:6px;margin-bottom:8px}
.nav b{display:block;color:#111;font-size:12px}
.msgs{display:flex;flex-direction:column;gap:6px}
.b{max-width:80%;padding:7px 10px;border-radius:15px;font-size:11.5px;line-height:1.35}
.biz{align-self:flex-start;background:#e9e9eb;color:#111;border-bottom-left-radius:4px}
.cust{align-self:flex-end;background:#2f7bf6;color:#fff;border-bottom-right-radius:4px}
.human{align-self:flex-start;background:#d9ead9;color:#111;border-bottom-left-radius:4px}
.chips{display:flex;flex-wrap:wrap;gap:5px;align-self:flex-start;max-width:92%}
.chip{border:1px solid #2f7bf6;color:#2f7bf6;border-radius:14px;padding:4px 9px;font-size:10.5px}
.lp{align-self:flex-start;width:92%;border:1px solid #e3e7ec;border-radius:12px;overflow:hidden}
.lp .row{padding:7px 9px;border-bottom:1px solid #eef1f4;font-size:11px;display:flex;align-items:center;gap:6px}
.lp .row:last-child{border-bottom:0}
.lp .thumb{width:16px;height:16px;border-radius:4px;background:#cfd6de}
.card{align-self:flex-start;width:92%;border:1px solid #e3e7ec;border-radius:12px;padding:9px;font-size:11px}
.card .k{font-size:9px;text-transform:uppercase;letter-spacing:.06em;color:#9aa4b1}
.cap{margin-top:7px;font-size:10.5px;color:#55606e}
.cap .step{font-weight:700;color:#16375c}
.cap .refs{font-family:ui-monospace,monospace;color:#8a929c}
.cap.block{color:#b42318}
.badge{display:inline-block;font-size:9px;font-weight:700;color:#b42318;border:1px solid #f0c2bd;border-radius:4px;padding:0 4px;margin-left:5px}
@media print{body{background:#fff}}
"""


def _bubble(step: dict) -> str:
    actor = step.get("actor", "bot")
    side = "cust" if actor == "customer" else ("human" if actor == "human" else "biz")
    k = step["kind"]
    copy = _esc(step.get("copy"))
    if k == "quick_reply":
        chips = "".join(f'<span class="chip">{_esc(o)}</span>' for o in step.get("options", []))
        return f'<div class="b {side}">{copy}</div><div class="chips">{chips}</div>'
    if k == "list_picker":
        rows = "".join(f'<div class="row"><span class="thumb"></span>{_esc(o)}</div>' for o in step.get("options", []))
        return f'<div class="b {side}">{copy}</div><div class="lp">{rows}</div>'
    if k in ("auth", "apple_pay", "time_picker", "rich_link"):
        label = {"auth": "Authentication", "apple_pay": "Apple Pay", "time_picker": "Time Picker", "rich_link": "Rich Link"}[k]
        return f'<div class="card"><div class="k">{label}</div>{copy}</div>'
    return f'<div class="b {side}">{copy}</div>'


def _frame(brand: str, step: dict, n: int, blockers: list[str]) -> str:
    refs = " ".join(refs_for(step))
    bad = bool(blockers)
    badge = ' <span class="badge">BLOCKER</span>' if bad else ""
    bmsg = (" — " + "; ".join(blockers)) if bad else ""
    return (f'<div class="cell"><div class="phone"><div class="nav"><b>{_esc(brand)}</b>Apple Messages for Business</div>'
            f'<div class="msgs">{_bubble(step)}</div></div>'
            f'<div class="cap{" block" if bad else ""}"><span class="step">{n}. {_esc(step.get("actor"))}/{_esc(step["kind"])}</span>'
            f'{badge} <span class="refs">{refs}</span>{_esc(bmsg)}</div></div>')


def render_html(flow_data: dict, blockers_by_key: dict, self_check: list[str]) -> str:
    brand = flow_data.get("brand", "Brand")
    out = [f'<!DOCTYPE html><html><head><meta charset="utf-8"><title>Storyboard — {_esc(brand)}</title>',
           f"<style>{CSS}</style></head><body>",
           f"<h1>UX Storyboard — {_esc(brand)}</h1>",
           '<div class="sub">Apple Messages for Business · conversation layout for UX approval</div>']
    titles = {"A": "Flow A — use case end to end", "B": "Flow B — human handoff", "C": "Flow C — degraded (out-of-hours / fallback)"}
    for fkey, steps in flow_data.get("flows", {}).items():
        out.append(f"<h2>{_esc(titles.get(fkey, 'Flow ' + fkey))}</h2><div class='flow'>")
        for i, step in enumerate(steps, 1):
            out.append(_frame(brand, step, i, blockers_by_key.get(f"{fkey}:{i}", [])))
        out.append("</div>")
    out.append("<h2>Standards 2.18 self-check</h2><ul>")
    out += [f"<li>{_esc(x)}</li>" for x in self_check]
    out.append("</ul></body></html>")
    return "\n".join(out)
