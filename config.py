from enum import Enum
from typing import TypedDict, List


class FontID(Enum):
    MOON_TIME_REGULAR = "fonts/MoonTime-Regular-1.ttf"
    NOW_REGULAR = "fonts/Now-Regular.otf"
    FUTURA = "fonts/FuturaCyrillicLight.ttf"
    NIXIE_ONE = "fonts/NixieOne.ttf"
    SEASONS = "fonts/The Seasons Regular.ttf"
    WEDGES = "fonts/Wedges.ttf"


class FontConfig(TypedDict):
    font: FontID
    size: int


class Background(TypedDict):
    id: str
    name: str
    path: str
    color: str
    title: FontConfig       # name at top of chart
    subtitle: FontConfig    # date at top of chart
    symbol_size: int        # zodiac glyph size (unicode, no font file)
    sign_name: FontConfig   # e.g. "Aries", "Tauro" in special_points
    point_label: FontConfig # "Sol", "Luna", "Ascendente" in special_points


BACKGROUNDS: List[Background] = [
    {
        "id": "noche_estrellada", "name": "Noche del Lobo",
        "path": "backgrounds/background.jpg", "color": "white",
        "title":       {"font": FontID.MOON_TIME_REGULAR, "size": 78},
        "subtitle":    {"font": FontID.NOW_REGULAR,        "size": 15},
        "symbol_size": 60,
        "sign_name":   {"font": FontID.NOW_REGULAR,        "size": 20},
        "point_label": {"font": FontID.MOON_TIME_REGULAR,  "size": 30},
    },
    {
        "id": "nebulosa", "name": "Nebulosa",
        "path": "backgrounds/background2.jpg", "color": "white",
        "title":       {"font": FontID.MOON_TIME_REGULAR, "size": 78},
        "subtitle":    {"font": FontID.NOW_REGULAR,        "size": 15},
        "symbol_size": 60,
        "sign_name":   {"font": FontID.NOW_REGULAR,        "size": 20},
        "point_label": {"font": FontID.MOON_TIME_REGULAR,  "size": 30},
    },
    {
        "id": "minimal_rosa", "name": "Minimalista rosa",
        "path": "backgrounds/minimalista-rosa.jpg", "color": "#fb868c",
        "title":       {"font": FontID.FUTURA,    "size": 76},
        "subtitle":    {"font": FontID.NOW_REGULAR, "size": 15},
        "symbol_size": 63,
        "sign_name":   {"font": FontID.NOW_REGULAR, "size": 25},
        "point_label": {"font": FontID.FUTURA,      "size": 18},
    },
    {
        "id": "negro", "name": "Negro",
        "path": "backgrounds/black.jpg", "color": "white",
        "title":       {"font": FontID.MOON_TIME_REGULAR, "size": 78},
        "subtitle":    {"font": FontID.NOW_REGULAR,        "size": 15},
        "symbol_size": 60,
        "sign_name":   {"font": FontID.NOW_REGULAR,        "size": 20},
        "point_label": {"font": FontID.MOON_TIME_REGULAR,  "size": 30},
    },
    {
        "id": "verde", "name": "Verde",
        "path": "backgrounds/green.jpg", "color": "white",
        "title":       {"font": FontID.FUTURA,    "size": 76},
        "subtitle":    {"font": FontID.NOW_REGULAR, "size": 15},
        "symbol_size": 63,
        "sign_name":   {"font": FontID.NOW_REGULAR, "size": 25},
        "point_label": {"font": FontID.FUTURA,      "size": 18},
    },
    {
        "id": "azul_estrella", "name": "Azul estrella",
        "path": "backgrounds/blue-stars.jpg", "color": "white",
        "title":       {"font": FontID.FUTURA,    "size": 76},
        "subtitle":    {"font": FontID.NIXIE_ONE,  "size": 15},
        "symbol_size": 63,
        "sign_name":   {"font": FontID.NIXIE_ONE,  "size": 25},
        "point_label": {"font": FontID.FUTURA,     "size": 18},
    },
    {
        "id": "gold", "name": "Gold",
        "path": "backgrounds/gold.jpg", "color": "#d4b68e",
        "title":       {"font": FontID.MOON_TIME_REGULAR, "size": 78},
        "subtitle":    {"font": FontID.NIXIE_ONE,  "size": 15},
        "symbol_size": 60,
        "sign_name":   {"font": FontID.MOON_TIME_REGULAR,  "size": 28},
        "point_label": {"font": FontID.MOON_TIME_REGULAR,  "size": 30},
    },
    {
        "id": "beige", "name": "Beige",
        "path": "backgrounds/beige.jpg", "color": "#805010",
        "title":       {"font": FontID.SEASONS,   "size": 76},
        "subtitle":    {"font": FontID.NOW_REGULAR, "size": 15},
        "symbol_size": 49,
        "sign_name":   {"font": FontID.NOW_REGULAR, "size": 21},
        "point_label": {"font": FontID.SEASONS,     "size": 14},
    },
    {
        "id": "aesthetic_retro_místico", "name": "Retro Místico",
        "path": "backgrounds/aesthetic_retro_místico.png", "color": "white",
        "title":       {"font": FontID.SEASONS,   "size": 76},
        "subtitle":    {"font": FontID.NOW_REGULAR, "size": 15},
        "symbol_size": 49,
        "sign_name":   {"font": FontID.NOW_REGULAR, "size": 21},
        "point_label": {"font": FontID.FUTURA,     "size": 18},
    },
    {
        "id": "nursery_dreams", "name": "Nursery dreams",
        "path": "backgrounds/nursery_dreams.png", "color": "#5D574F",
        "title":       {"font": FontID.SEASONS,   "size": 76},
        "subtitle":    {"font": FontID.NOW_REGULAR, "size": 15},
        "symbol_size": 49,
        "sign_name":   {"font": FontID.NOW_REGULAR, "size": 21},
        "point_label": {"font": FontID.NIXIE_ONE,     "size": 18},
    },
]
