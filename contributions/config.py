import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.getenv("VIRTUAL_ENV", None)
FONTS_PATH = os.path.join(BASE_DIR, "fonts")
if PATH:
    FONTS_PATH = os.path.join(BASE_DIR, "contributions", "fonts")

WEEKDAY = {
    0: 7,
    1: 6,
    2: 5,
    3: 4,
    4: 3,
    5: 2,
    6: 1
}
