# config.py
# ─────────────────────────────────────────────
# All constants live here — fonts, quotes,
# words, and themes. Easy to edit in one place.
# ─────────────────────────────────────────────

# ── Fonts (Windows paths) ──────────────────────
FONTS = {
    "bold":   "C:/Windows/Fonts/georgiab.ttf",
    "italic": "C:/Windows/Fonts/georgiai.ttf",
    "reg":    "C:/Windows/Fonts/georgiai.ttf",
    "sans":   "C:/Windows/Fonts/trebuc.ttf",
}

# ── Empowerment words ──────────────────────────
WORDS = [
    "FIERCE",
    "RADIANT",
    "FEARLESS",
    "LIMITLESS",
    "UNSTOPPABLE",
    "POWERFUL",
    "LUMINOUS",
]

# ── Quotes pool ────────────────────────────────
QUOTES = [
    ("There is no limit to what we,\nas women, can accomplish.",  "Michelle Obama"),
    ("Well-behaved women seldom\nmake history.",                   "Laurel Thatcher Ulrich"),
    ("She believed she could,\nso she did.",                       "R.S. Grey"),
    ("The most courageous act is still\nto think for yourself.",   "Coco Chanel"),
    ("A woman with a voice is,\nby definition, a strong woman.",   "Melinda Gates"),
    ("You are more powerful than\nyou know.",                      "Melissa Etheridge"),
]

# ── Card themes ────────────────────────────────
# Each theme has:
#   bg      → background color  (dark, for the card)
#   accent  → main color        (used for borders, highlights)
#   accent2 → softer version    (used for secondary elements)
THEMES = {
    "rose": {
        "bg":      (12,  8, 10),
        "accent":  (255, 80, 120),
        "accent2": (255, 140, 160),
    },
    "gold": {
        "bg":      (10,  8,  4),
        "accent":  (220, 170, 60),
        "accent2": (255, 210, 100),
    },
    "mauve": {
        "bg":      (14,  8, 14),
        "accent":  (195, 130, 175),
        "accent2": (220, 165, 205),
    },
    "champagne": {
        "bg":      (14, 11,  6),
        "accent":  (210, 175, 110),
        "accent2": (235, 205, 155),
    },
}
