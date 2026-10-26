"""
Render the storyboard slide model into the Linq/Juno submission deck, drawn to look
like real Apple Messages for Business screens:
- iOS Messages chrome (status bar, nav with brand avatar, bubble tails).
- The thread DEVELOPS: within a use-case slide, each frame shows the whole
  conversation accumulated up to that step (not one isolated bubble).
- Rich elements are rendered for real (Quick Reply chips, List Picker rows,
  Time Picker, Rich Link card w/ image, Apple Pay sheet, Authentication card,
  typing indicator) — not labeled boxes.
- Steps with no Messages screen (phone:false — entry points, web signup) render
  with NO phone, just the caption. HTML; print to PDF.
"""
from __future__ import annotations
import html

try:
    import amb_assets
except Exception:
    amb_assets = None

# Element kinds shown as a real full-screen Apple sheet (composed from the Figma
# library) rather than an in-thread CSS bubble. The rest (text, quick_reply,
# rich_link, typing) stay in the developing CSS thread.
FULLSCREEN = {"list_picker", "time_picker", "auth"}


def _esc(s):
    return html.escape(str(s or ""))

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:#eef1f4;color:#1b2430;padding:28px}
.slide{background:#fff;border-radius:14px;box-shadow:0 2px 10px rgba(0,0,0,.08);padding:28px 32px;margin:0 auto 24px;max-width:1320px}
.cover h1{font-size:30px;font-weight:800;color:#16375c}
.cover .sub{color:#6b7280;margin:6px 0 16px;font-size:14px}
.cover .fmt{background:#f6f8fa;border:1px solid #e3e7ec;border-radius:10px;padding:14px 16px;font-size:13px;color:#374151;line-height:1.5;margin-bottom:14px}
.uclist{display:flex;gap:10px;flex-wrap:wrap}.uccard{border:1px solid #e3e7ec;border-radius:10px;padding:10px 12px;min-width:200px}.uccard b{color:#16375c;font-size:13px}
h2{font-size:19px;font-weight:800;color:#16375c}.desc{color:#55606e;font-size:13px;margin:4px 0 16px;max-width:980px;line-height:1.45}
.steps{display:flex;gap:16px;overflow-x:auto;padding-bottom:6px}
.step{width:236px;flex:0 0 236px;display:flex;flex-direction:column}
.stephead{font-size:10px;font-weight:700;letter-spacing:.05em;color:#8a929c;text-transform:uppercase}
.tag{display:inline-block;font-size:10px;font-weight:700;border-radius:5px;padding:1px 6px;margin:5px 0}
.tag.feature{background:#efe7fb;color:#6b3fd1;border:1px solid #d9c7f4}.tag.req{background:#fdeeea;color:#b4521e;border:1px solid #f3cdbd}.tag.entry{background:#e7f1fb;color:#2f6db0;border:1px solid #c6ddf2}
.stepdesc{font-size:11.5px;color:#374151;margin:4px 0 9px;line-height:1.4;min-height:40px}
.nophone{border:1px dashed #d8dee6;border-radius:14px;height:150px;display:flex;align-items:center;justify-content:center;color:#b0b8c1;font-size:11px;text-align:center;padding:12px}
/* iPhone */
.phone{background:#fff;border:9px solid #0a0a0a;border-radius:34px;height:430px;overflow:hidden;position:relative;box-shadow:0 5px 16px rgba(0,0,0,.14)}
.sbar{display:flex;justify-content:space-between;align-items:center;padding:6px 16px 2px;font-size:10px;font-weight:600;color:#111}
.sbar .r{letter-spacing:1px}
.nav{display:flex;flex-direction:column;align-items:center;padding:3px 0 7px;border-bottom:.5px solid #e2e2e4;position:relative}
.nav .av{width:30px;height:30px;border-radius:30px;background:#16375c;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:13px}
.nav .nm{font-size:10px;color:#111;margin-top:2px;display:flex;align-items:center;gap:2px}
.nav .back{position:absolute;left:12px;top:8px;color:#2f7bf6;font-size:17px}
.thread{height:330px;padding:9px 9px 12px;display:flex;flex-direction:column;justify-content:flex-end;gap:4px;overflow:hidden}
.row{display:flex;flex-direction:column}
.b{max-width:80%;padding:6px 10px;border-radius:17px;font-size:11px;line-height:1.35;word-wrap:break-word}
.bot{align-self:flex-start;background:#e9e9ea;color:#111;border-bottom-left-radius:5px}
.user{align-self:flex-end;background:#8e95a2;color:#fff;border-bottom-right-radius:5px}
.chips{align-self:flex-start;display:flex;flex-wrap:wrap;gap:5px;max-width:92%;margin-top:1px}
.chip{border:1px solid #3797f0;color:#3797f0;border-radius:15px;padding:4px 10px;font-size:10px;background:#fff}
.lp{align-self:flex-start;width:94%;background:#fff;border:1px solid #e3e7ec;border-radius:13px;overflow:hidden}
.lp .t{font-size:10px;font-weight:700;color:#111;padding:7px 10px;border-bottom:1px solid #eef1f4;background:#f7f8fa}
.lp .r{display:flex;align-items:center;gap:8px;padding:7px 10px;border-bottom:1px solid #f1f3f5}
.lp .r:last-child{border-bottom:0}.lp .th{width:26px;height:26px;border-radius:6px;background:linear-gradient(135deg,#cdd5de,#aab4c0);flex:0 0 26px}
.lp .tt{font-size:10.5px;color:#111;font-weight:600}.lp .ss{font-size:9px;color:#8a929c}.lp .cv{margin-left:auto;color:#c3cad3}
.tp{align-self:flex-start;width:94%;background:#fff;border:1px solid #e3e7ec;border-radius:13px;padding:9px}
.tp .t{font-size:10px;font-weight:700;color:#111;margin-bottom:6px}.tp .opts{display:flex;flex-wrap:wrap;gap:5px}
.tp .o{border:1px solid #cfd6de;border-radius:8px;padding:4px 8px;font-size:9.5px;color:#374151}
.rl{align-self:flex-start;width:84%;background:#fff;border:1px solid #e3e7ec;border-radius:13px;overflow:hidden}
.rl .img{height:74px;background:linear-gradient(135deg,#2f6db0,#16375c);display:flex;align-items:center;justify-content:center;color:rgba(255,255,255,.85);font-size:9px;text-align:center;padding:6px}
.rl .meta{padding:7px 10px}.rl .tt{font-size:10.5px;font-weight:600;color:#111}.rl .dm{font-size:9px;color:#8a929c;text-transform:lowercase}
.ap{align-self:flex-start;width:84%;background:#000;color:#fff;border-radius:13px;padding:9px 11px}
.ap .m{font-size:9px;opacity:.7}.ap .a{font-size:14px;font-weight:700;margin:2px 0 7px}
.ap .pay{background:#fff;color:#000;border-radius:7px;text-align:center;font-size:11px;font-weight:700;padding:5px 0}
.au{align-self:flex-start;width:84%;background:#fff;border:1px solid #e3e7ec;border-radius:13px;padding:11px;text-align:center}
.au .lk{font-size:16px}.au .tx{font-size:10px;color:#374151;margin:4px 0 8px}.au .btn{background:#3797f0;color:#fff;border-radius:8px;font-size:10.5px;font-weight:600;padding:6px 0}
.typing{align-self:flex-start;background:#e9e9ea;border-radius:15px;padding:8px 12px;display:flex;gap:3px}
.typing i{width:6px;height:6px;border-radius:6px;background:#9aa0a6;display:inline-block}
.ambscreen{width:100%;border-radius:18px;display:block;box-shadow:0 5px 16px rgba(0,0,0,.14)}
.cap{margin-top:8px;font-size:10.5px;color:#55606e}.cap .st{font-weight:700;color:#16375c}
@media print{body{background:#fff}.slide{box-shadow:none;break-inside:avoid;page-break-after:always}}
"""


def _item(it: dict) -> str:
    side = "user" if it.get("side") == "user" else "bot"
    kind = it.get("kind")
    if not kind:  # plain bubble
        return f'<div class="b {side}">{_esc(it.get("text"))}</div>'
    framing = f'<div class="b bot">{_esc(it.get("text"))}</div>' if it.get("text") else ""
    if kind == "quick_reply":
        chips = "".join(f'<span class="chip">{_esc(o)}</span>' for o in it.get("options", []))
        return framing + f'<div class="chips">{chips}</div>'
    if kind == "list_picker":
        rows = "".join(f'<div class="r"><span class="th"></span><div><div class="tt">{_esc(r.get("title"))}</div>'
                       f'<div class="ss">{_esc(r.get("subtitle"))}</div></div><span class="cv">›</span></div>'
                       for r in it.get("rows", []))
        return framing + f'<div class="lp"><div class="t">{_esc(it.get("title") or "Select")}</div>{rows}</div>'
    if kind == "time_picker":
        opts = "".join(f'<span class="o">{_esc(o)}</span>' for o in it.get("options", []))
        return framing + f'<div class="tp"><div class="t">Pick a time</div><div class="opts">{opts}</div></div>'
    if kind == "rich_link":
        return (framing + f'<div class="rl"><div class="img">{_esc(it.get("image") or "preview")}</div>'
                f'<div class="meta"><div class="tt">{_esc(it.get("title"))}</div>'
                f'<div class="dm">{_esc(it.get("domain"))}</div></div></div>')
    if kind == "apple_pay":
        return (framing + f'<div class="ap"><div class="m">{_esc(it.get("merchant"))}</div>'
                f'<div class="a">{_esc(it.get("amount"))}</div><div class="pay"> Pay</div></div>')
    if kind == "auth":
        return (framing + '<div class="au"><div class="lk">🔒</div>'
                '<div class="tx">Verify your identity to continue</div><div class="btn">Sign In</div></div>')
    if kind == "typing":
        return '<div class="typing"><i></i><i></i><i></i></div>'
    return framing or f'<div class="b {side}">{_esc(it.get("text"))}</div>'


def _phone(brand: str, thread: list[dict]) -> str:
    av = (brand or "?")[:1].upper()
    body = "".join(f'<div class="row">{_item(it)}</div>' for it in thread)
    return (f'<div class="phone"><div class="sbar"><span>9:41</span><span class="r">●●● ▪ 100%</span></div>'
            f'<div class="nav"><span class="back">‹</span><span class="av">{_esc(av)}</span>'
            f'<span class="nm">{_esc(brand)} ›</span></div>'
            f'<div class="thread">{body}</div></div>')


def _compose_screen(brand: str, color: str, el: dict, out_dir: str) -> str | None:
    """Composite a real full-screen AMB element; return PNG path (rel to out_dir) or None."""
    if not amb_assets:
        return None
    kind = el.get("kind")
    kw = {"color": color, "out_dir": out_dir}
    if kind == "list_picker":
        kw["rows"] = el.get("rows") or []
        kw["title"] = el.get("title") or ""
    elif kind == "time_picker":
        kw["title"] = el.get("text") or f"Schedule with {brand}"
    try:
        return amb_assets.compose(kind, brand, **kw)
    except Exception:
        return None


def _step_col(brand: str, color: str, i: int, step: dict, thread: list[dict], fs: dict | None, out_dir: str) -> str:
    tag = step.get("tag") or {}
    tag_html = ""
    if tag.get("text"):
        t = (tag.get("type") or "").lower()
        cls = "feature" if "feature" in t else "req" if "require" in t else "entry" if "entry" in t else "feature"
        tag_html = f'<span class="tag {cls}">{_esc(tag.get("type"))}: {_esc(tag.get("text"))}</span>'
    # Priority: a real full-screen element → the developing CSS thread → no phone.
    phone = ""
    if step.get("phone") and fs:
        img = _compose_screen(brand, color, fs, out_dir)
        phone = (f'<img class="ambscreen" src="{_esc(img)}" alt="{_esc(fs.get("kind"))}">'
                 if img else _phone(brand, thread + [fs]))
    elif step.get("phone") and thread:
        phone = _phone(brand, thread)
    return (f'<div class="step">{phone}'
            f'<div class="cap"><span class="st">STEP {i} · {_esc(step.get("mode","USER DOES"))}</span></div>'
            f'{tag_html}<div class="stepdesc">{_esc(step.get("description"))}</div></div>')


def render_html(model: dict, out_dir: str = "") -> str:
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
           '<div class="fmt">Each use case is shown as the Messages thread as it develops — step by step, '
           'with the real Apple elements (Quick Reply, List Picker, Time Picker, Rich Link, Apple Pay, '
           'Authentication). Purple tags are the Apple features selected per use case.</div>',
           (f'<div style="margin:8px 0 4px;color:#55606e;font-size:13px">{_esc(cover.get("summary"))}</div>' if cover.get("summary") else ""),
           f'<div class="uclist">{uc_html}</div></div>']
    color = model.get("brand_color") or "#1676FF"
    for s in model.get("sections", []):
        thread: list[dict] = []
        cols = []
        for i, st in enumerate(s.get("steps", []), 1):
            fs = None
            if st.get("phone"):
                for a in st.get("adds") or []:
                    if a.get("kind") in FULLSCREEN:
                        fs = a                      # shown as its own full-screen sheet
                    else:
                        thread = thread + [a]       # text / quick_reply / rich_link accumulate
            cols.append(_step_col(brand, color, i, st, thread, fs, out_dir))
        out.append(f'<div class="slide"><h2>{_esc(s.get("title"))}</h2>'
                   f'<div class="desc">{_esc(s.get("description"))}</div>'
                   f'<div class="steps">{"".join(cols)}</div></div>')
    out.append("</body></html>")
    return "\n".join(out)
