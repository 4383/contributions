import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.getenv("VIRTUAL_ENV", None)
FONTS_PATH = os.path.join(BASE_DIR, "fonts")
if PATH:
    FONTS_PATH = os.path.join(BASE_DIR, "contributions", "fonts")

WEEKDAY = {
    0: 9,
    1: 8,
    2: 7,
    3: 6,
    4: 5,
    5: 4,
    6: 3
}
