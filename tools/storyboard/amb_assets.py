"""
Compose brand-specific AMB element screens by overlaying brand data (name, logo,
title, rows/times) onto the official Messaging Advisory screens mirrored from Figma
(assets/amb-figma/). The screens are flattened rasters using Apple's "Acme" brand,
so the renderer can't rely on editable layers — we cover the known regions and
redraw. Pixel-perfect Apple chrome + the real brand's content.

Coordinates are fractions of the 1428x2919 source frame (so they survive a scale
change). Output is cached to assets/amb-composed/<brand-slug>/<kind>.png and the
storyboard renderer references it with an <img>. Falls back silently (returns None)
if Pillow or the source asset is missing — render_deck then uses its CSS element.
"""
from __future__ import annotations
import os, re

HERE = os.path.dirname(__file__)
FIGMA = os.path.join(HERE, "assets", "amb-figma")
OUT = os.path.join(HERE, "assets", "amb-composed")

# element kind -> source frame (expanded, "real as on the phone" view)
SOURCE = {
    "list_picker": "02_AMB_Elements_List_Picker_Open",
    "time_picker": "02_AMB_Elements_Time_Picker_Open",
    "auth": "02_AMB_Elements_OAuth2_Login",
    "apple_pay": "01_AMB_Elements_ApplePay_Payment",
}

# List Picker Open: 5 rows, each with icon tile + title + subtitle. Fractions of H.
LP_ROW_TOP = [0.245, 0.356, 0.468, 0.578, 0.690]
LP_ROW_H = 0.098
LP_ICON_X = (0.085, 0.205)       # icon tile x-range (fraction of W)
LP_TEXT_X = 0.235                # text left
LP_TEXT_R = 0.92                 # text right (cover up to here)

# Time Picker Open: the only brand-specific text is the title block at the top
# ("Schedule your Acme Car rental pickup time" / "Tap to select"). The slot buttons
# below already show generic example times, so we leave them untouched.
TP_TITLE = (0.06, 0.122, 0.95, 0.215)          # x0,y0,x1,y1 cover+redraw region


def _slug(s):
    return re.sub(r"[^a-z0-9]+", "-", (s or "brand").lower()).strip("-")


def _font(sz, bold=False):
    from PIL import ImageFont
    paths = (["/System/Library/Fonts/SFNS.ttf", "/Library/Fonts/Arial Bold.ttf",
              "/System/Library/Fonts/Supplemental/Arial Bold.ttf"] if bold else
             ["/System/Library/Fonts/SFNS.ttf", "/Library/Fonts/Arial.ttf",
              "/System/Library/Fonts/Supplemental/Arial.ttf"])
    for p in paths:
        try:
            return ImageFont.truetype(p, sz)
        except Exception:
            pass
    return ImageFont.load_default()


def _wrap(d, text, font, max_w):
    words, lines, cur = (text or "").split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= max_w or not cur:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur:
        lines.append(cur)
    return lines or [""]


def _tile(d, box, color, letter):
    x0, y0, x1, y1 = box
    r = int((y1 - y0) * 0.26)
    d.rounded_rectangle(box, radius=r, fill=color)
    f = _font(int((y1 - y0) * 0.55), bold=True)
    tb = d.textbbox((0, 0), letter, font=f)
    d.text(((x0 + x1) / 2 - (tb[2] - tb[0]) / 2, (y0 + y1) / 2 - (tb[3] - tb[1]) / 2 - tb[1]),
           letter, font=f, fill="white")


def _brand_rgb(hexs):
    if hexs and re.fullmatch(r"#?[0-9a-fA-F]{6}", hexs):
        h = hexs.lstrip("#")
        return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
    return (23, 118, 255)


def compose(kind: str, brand: str, *, title: str = "", rows=None,
            amount: str = "", color: str = "", out_dir: str = "") -> str | None:
    """Compose a brand element screen. Writes under out_dir (co-located with the deck
    HTML) when given — returns the path relative to out_dir; otherwise writes to the
    module cache and returns a path relative to tools/storyboard. None → fall back."""
    try:
        from PIL import Image, ImageDraw
    except Exception:
        return None
    src = os.path.join(FIGMA, SOURCE.get(kind, "") + ".png") if kind in SOURCE else ""
    if not src or not os.path.exists(src):
        return None
    im = Image.open(src).convert("RGB")
    W, H = im.size
    d = ImageDraw.Draw(im)
    accent = _brand_rgb(color)

    if kind == "list_picker":
        rows = (rows or [])[:5]
        for i, row in enumerate(rows):
            top = LP_ROW_TOP[i] * H
            # cover old icon + text
            d.rectangle([LP_ICON_X[0] * W, top, LP_TEXT_R * W, top + LP_ROW_H * H], fill="white")
            _tile(d, (LP_ICON_X[0] * W, top + 0.012 * H, LP_ICON_X[1] * W, top + LP_ROW_H * H - 0.012 * H),
                  accent, (row.get("title") or "?")[:1].upper())
            tf, sf = _font(int(0.034 * W), bold=True), _font(int(0.027 * W))
            d.text((LP_TEXT_X * W, top + 0.012 * H), (row.get("title") or "")[:34], font=tf, fill=(17, 17, 17))
            d.text((LP_TEXT_X * W, top + 0.052 * H), (row.get("subtitle") or "")[:44], font=sf, fill=(120, 126, 134))

    elif kind == "time_picker":
        x0, y0, x1, y1 = (TP_TITLE[0] * W, TP_TITLE[1] * H, TP_TITLE[2] * W, TP_TITLE[3] * H)
        d.rectangle([x0, y0, x1, y1], fill="white")
        tf, sf = _font(int(0.050 * W), bold=True), _font(int(0.032 * W))
        lines = _wrap(d, title or f"Schedule with {brand}", tf, x1 - x0)[:2]
        ly = y0
        for ln in lines:
            d.text((x0, ly), ln, font=tf, fill=(17, 17, 17)); ly += 0.050 * H
        d.text((x0, ly + 0.004 * H), "Tap to select", font=sf, fill=(140, 146, 154))

    elif kind == "apple_pay":
        # merchant line near top of the pay sheet
        d.rectangle([0.30 * W, 0.11 * H, 0.70 * W, 0.155 * H], fill="white")
        mf = _font(int(0.04 * W), bold=True)
        mb = d.textbbox((0, 0), brand, font=mf)
        d.text((W / 2 - (mb[2] - mb[0]) / 2, 0.11 * H), brand, font=mf, fill=(17, 17, 17))

    elif kind == "auth":
        pass  # login page is brand-neutral; header handled upstream

    if out_dir:
        rel = os.path.join("amb-assets", _slug(brand), f"{kind}.png")
        dest = os.path.join(out_dir, rel)
    else:
        rel = os.path.join("assets", "amb-composed", _slug(brand), f"{kind}.png")
        dest = os.path.join(HERE, rel)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    im.save(dest)
    return rel
