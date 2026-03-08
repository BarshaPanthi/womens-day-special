# card.py
# ─────────────────────────────────────────────
# Responsible for ONE thing only:
# Drawing the card image using Pillow.
# Call make_card(name, theme) → get PNG bytes.
# ─────────────────────────────────────────────

from PIL import Image, ImageDraw, ImageFont
import math, io, random
from config import FONTS, WORDS, QUOTES, THEMES


def _draw_centered(draw, text, y, font, fill, W=1080):
    """Draw text horizontally centered on the canvas."""
    bbox = draw.textbbox((0, 0), text, font=font)
    tw   = bbox[2] - bbox[0]
    draw.text(((W - tw) // 2, y), text, font=font, fill=fill)


def _draw_background(img, bg):
    """Draw a subtle dark gradient from top to bottom."""
    draw = ImageDraw.Draw(img)
    W, H = img.size
    for y in range(H):
        frac = y / H
        draw.line([(0, y), (W, y)], fill=(
            int(bg[0] + 18 * frac),
            int(bg[1] +  4 * frac),
            int(bg[2] + 14 * frac),
        ))


def _draw_glow(img, bg, accent):
    """Blend a soft radial glow in the center of the image."""
    W, H   = img.size
    cx, cy = W // 2, H // 2
    glow   = Image.new("RGB", (W, H), (0, 0, 0))
    gd     = ImageDraw.Draw(glow)
    for r in range(380, 0, -1):
        a = int(22 * (1 - r / 380))
        gd.ellipse([cx-r, cy-r, cx+r, cy+r], fill=(
            min(255, bg[0] + accent[0] * a // 40),
            min(255, bg[1] + accent[1] * a // 40),
            min(255, bg[2] + accent[2] * a // 40),
        ))
    return Image.blend(img, glow, 0.55)


def _draw_rings(draw, W, H, accent):
    """Draw concentric dot rings using cos/sin math."""
    cx, cy = W // 2, H // 2
    for i in range(9):
        radius = 150 + i * 88
        for angle in range(0, 360, 2):
            rd = math.radians(angle)
            draw.point(
                (cx + radius * math.cos(rd), cy + radius * math.sin(rd)),
                fill=accent
            )


def _draw_border(draw, W, H, accent, accent2):
    """Draw double border frame with corner flourishes."""
    p = 72
    draw.rectangle([p,    p,    W-p,    H-p   ], outline=accent,  width=1)
    draw.rectangle([p+10, p+10, W-p-10, H-p-10], outline=accent2, width=1)
    s = 22
    for (ox, oy), (dx, dy) in [
        ((p,   p  ), ( 1,  1)), ((W-p, p  ), (-1,  1)),
        ((p,   H-p), ( 1, -1)), ((W-p, H-p), (-1, -1)),
    ]:
        draw.line([(ox, oy), (ox + dx*s, oy)],       fill=accent, width=2)
        draw.line([(ox, oy), (ox,        oy + dy*s)], fill=accent, width=2)


def _draw_text(draw, name, accent, accent2, W, H):
    """Draw all text layers: date, name, word, quote, hashtags."""
    cx = W // 2

    f_tiny  = ImageFont.truetype(FONTS["sans"],   20)
    f_small = ImageFont.truetype(FONTS["sans"],   23)
    f_she   = ImageFont.truetype(FONTS["reg"],    30)
    f_name  = ImageFont.truetype(FONTS["italic"], min(108, max(54, 108 - max(0, len(name)-7)*7)))
    f_word  = ImageFont.truetype(FONTS["bold"],   46)
    f_quote = ImageFont.truetype(FONTS["reg"],    31)
    f_attr  = ImageFont.truetype(FONTS["sans"],   21)

    _draw_centered(draw, "MARCH 8  ·  INTERNATIONAL WOMEN'S DAY", 140, f_small, accent)
    draw.line([cx-120, 188, cx+120, 188], fill=accent, width=1)
    _draw_centered(draw, "This card is for", 210, f_she, (200, 200, 200))

    name_display = name.title()
    bbox   = draw.textbbox((0, 0), name_display, font=f_name)
    name_w = bbox[2] - bbox[0]
    nx     = (W - name_w) // 2
    draw.text((nx+3, 281), name_display, font=f_name, fill=(0, 0, 0))
    draw.text((nx,   278), name_display, font=f_name, fill=(255, 255, 255))
    draw.line([nx, 395, nx+name_w, 395], fill=accent, width=2)

    _draw_centered(draw, f"— {random.choice(WORDS)} —", 428, f_word, accent2)
    draw.line([cx-40, 498, cx+40, 498], fill=accent, width=1)

    quote_text, quote_attr = random.choice(QUOTES)
    lines = quote_text.split("\n")
    y_q   = 524
    for i, line in enumerate(lines):
        if i == 0:              line = f'"{line}'
        if i == len(lines) - 1: line = f'{line}"'
        _draw_centered(draw, line, y_q, f_quote, (220, 220, 220))
        y_q += 48
    _draw_centered(draw, f"— {quote_attr}", y_q + 8, f_attr, accent)

    dot_y   = 730
    pattern = [5, 5, 5, 5, 20, 5, 5, 5, 5]
    total   = sum(pattern) + 10 * (len(pattern) - 1)
    sx      = cx - total // 2
    for d in pattern:
        if d == 20:
            draw.ellipse([sx, dot_y-2, sx+d, dot_y+4], fill=accent)
        else:
            draw.ellipse([sx, dot_y, sx+d, dot_y+d], fill=(accent[0]//2, accent[1]//2, accent[2]//2))
        sx += d + 10

    _draw_centered(draw, "#IWD2026  ·  #InspireInclusion  ·  #WomensDay", 774, f_tiny,  (90, 90, 90))
    _draw_centered(draw, "You are extraordinary.", 840, f_she, (180, 180, 180))
    draw.line([cx-80, 888, cx+80, 888], fill=accent, width=1)


def make_card(name: str, theme: str = "rose") -> bytes:
    """Generate a 1080x1080 Women's Day card. Returns PNG bytes."""
    t       = THEMES.get(theme, THEMES["rose"])
    bg      = t["bg"]
    accent  = t["accent"]
    accent2 = t["accent2"]
    W, H    = 1080, 1080

    img = Image.new("RGB", (W, H), bg)
    _draw_background(img, bg)
    img  = _draw_glow(img, bg, accent)
    draw = ImageDraw.Draw(img)
    _draw_rings(draw, W, H, accent)
    _draw_border(draw, W, H, accent, accent2)
    _draw_text(draw, name, accent, accent2, W, H)

    buf = io.BytesIO()
    img.save(buf, "PNG")
    buf.seek(0)
    return buf.read()
