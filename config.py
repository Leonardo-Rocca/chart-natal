from enum import Enum
from typing import TypedDict


class FontID(Enum):
    MOON_TIME_REGULAR = "fonts/MoonTime-Regular-1.ttf"
    NOW_REGULAR = "fonts/Now-Regular.otf"
    FUTURA = "fonts/Futura Light.otf"
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


BACKGROUNDS: list[Background] = [
    {
        "id": "noche_estrellada", "name": "Noche Lobo",
        "path": "backgrounds/background.jpg", "color": "white",
        "title":       {"font": FontID.MOON_TIME_REGULAR, "size": 78},
        "subtitle":    {"font": FontID.NOW_REGULAR,        "size": 15},
        "symbol_size": 60,
        "sign_name":   {"font": FontID.NOW_REGULAR,        "size": 20},
        "point_label": {"font": FontID.MOON_TIME_REGULAR,  "size": 30},
    },
    {
        "id": "nebulosa", "name": "Nebulosa",
        "path": "backgrounds/nebulosa.png", "color": "white",
        "title":       {"font": FontID.MOON_TIME_REGULAR, "size": 78},
        "subtitle":    {"font": FontID.NOW_REGULAR,        "size": 15},
        "symbol_size": 60,
        "sign_name":   {"font": FontID.NOW_REGULAR,        "size": 20},
        "point_label": {"font": FontID.MOON_TIME_REGULAR,  "size": 30},
    },
    {
        "id": "azul_estrella", "name": "Azul estrella",
        "path": "backgrounds/blue-stars.jpg", "color": "white",
        "title":       {"font": FontID.FUTURA,    "size": 70},
        "subtitle":    {"font": FontID.NOW_REGULAR,  "size": 15},
        "symbol_size": 63,
        "sign_name":   {"font": FontID.NOW_REGULAR,  "size": 21},
        "point_label": {"font": FontID.NOW_REGULAR,     "size": 19},
    },
    {
        "id": "pintura_azul", "name": "Pintura Azul",
        "path": "backgrounds/pintura_azul.jpg", "color": "white",
        "title":       {"font": FontID.MOON_TIME_REGULAR,   "size": 76},
        "subtitle":    {"font": FontID.NIXIE_ONE, "size": 15},
        "symbol_size": 49,
        "sign_name":   {"font": FontID.MOON_TIME_REGULAR, "size": 41},
        "point_label": {"font": FontID.NIXIE_ONE,     "size": 14},
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
        "title":       {"font": FontID.FUTURA,    "size": 70},
        "subtitle":    {"font": FontID.NOW_REGULAR, "size": 15},
        "symbol_size": 63,
        "sign_name":   {"font": FontID.NOW_REGULAR, "size": 25},
        "point_label": {"font": FontID.FUTURA,      "size": 18},
    },
    {
        "id": "blue", "name": "Azul",
        "path": "backgrounds/blue.png", "color": "white",
        "title":       {"font": FontID.FUTURA,    "size": 70},
        "subtitle":    {"font": FontID.NOW_REGULAR, "size": 15},
        "symbol_size": 63,
        "sign_name":   {"font": FontID.NOW_REGULAR, "size": 25},
        "point_label": {"font": FontID.FUTURA,      "size": 18},
    },
    {
        "id": "purple", "name": "Purple",
        "path": "backgrounds/purple.png", "color": "white",
        "title":       {"font": FontID.FUTURA,    "size": 70},
        "subtitle":    {"font": FontID.NOW_REGULAR, "size": 15},
        "symbol_size": 63,
        "sign_name":   {"font": FontID.NOW_REGULAR, "size": 25},
        "point_label": {"font": FontID.FUTURA,      "size": 18},
    },
    {
        "id": "pink", "name": "Pink",
        "path": "backgrounds/pink.png", "color": "black",
        "title":       {"font": FontID.FUTURA,    "size": 70},
        "subtitle":    {"font": FontID.NOW_REGULAR, "size": 15},
        "symbol_size": 63,
        "sign_name":   {"font": FontID.NOW_REGULAR, "size": 25},
        "point_label": {"font": FontID.FUTURA,      "size": 18},
    },
    {
        "id": "gold", "name": "Gold",
        "path": "backgrounds/gold.jpg", "color": "#d4b68e",
        "title":       {"font": FontID.MOON_TIME_REGULAR, "size": 78},
        "subtitle":    {"font": FontID.NIXIE_ONE,  "size": 15},
        "symbol_size": 60,
        "sign_name":   {"font": FontID.NOW_REGULAR,  "size": 20},
        "point_label": {"font": FontID.MOON_TIME_REGULAR,  "size": 30},
    },
    {
        "id": "beige", "name": "Beige",
        "path": "backgrounds/beige.jpg", "color": "#805010",
        "title":       {"font": FontID.SEASONS,   "size": 66},
        "subtitle":    {"font": FontID.NOW_REGULAR, "size": 15},
        "symbol_size": 49,
        "sign_name":   {"font": FontID.NOW_REGULAR, "size": 21},
        "point_label": {"font": FontID.SEASONS,     "size": 19},
    },
    {
        "id": "nursery_dreams", "name": "Nursery dreams",
        "path": "backgrounds/nursery_dreams.png", "color": "#5D574F",
        "title":       {"font": FontID.SEASONS,   "size": 76},
        "subtitle":    {"font": FontID.NOW_REGULAR, "size": 15},
        "symbol_size": 49,
        "sign_name":   {"font": FontID.NOW_REGULAR, "size": 21},
        "point_label": {"font": FontID.NOW_REGULAR,     "size": 21},
    },
    {
        "id": "aesthetic_retro_mistico", "name": "Retro Místico",
        "path": "backgrounds/aesthetic_retro_mistico.png", "color": "white",
        "title":       {"font": FontID.SEASONS,   "size": 76},
        "subtitle":    {"font": FontID.NOW_REGULAR, "size": 15},
        "symbol_size": 49,
        "sign_name":   {"font": FontID.NOW_REGULAR, "size": 21},
        "point_label": {"font": FontID.FUTURA,     "size": 23},
    },
    {
        "id": "dark_academia", "name": "Dark Academia",
        "path": "backgrounds/dark_academia.jpg", "color": "#D4AF37",
        "title":       {"font": FontID.SEASONS,   "size": 76},
        "subtitle":    {"font": FontID.NOW_REGULAR, "size": 15},
        "symbol_size": 49,
        "sign_name":   {"font": FontID.NOW_REGULAR, "size": 25},
        "point_label": {"font": FontID.SEASONS,     "size": 18},
    },
    {
        "id": "pergamino", "name": "Pergamino",
        "path": "backgrounds/pergamino.jpg", "color": "#4A4A4A",
        "title":       {"font": FontID.SEASONS,    "size": 76},
        "subtitle":    {"font": FontID.NOW_REGULAR, "size": 15},
        "symbol_size": 63,
        "sign_name":   {"font": FontID.NOW_REGULAR, "size": 25},
        "point_label": {"font": FontID.SEASONS,      "size": 18},
    },
    {
        "id": "bosque", "name": "Bosque",
        "path": "backgrounds/bosque.jpg", "color": "#4A4A4A",
        "title":       {"font": FontID.SEASONS,   "size": 66},
        "subtitle":    {"font": FontID.NOW_REGULAR, "size": 15},
        "symbol_size": 49,
        "sign_name":   {"font": FontID.NOW_REGULAR, "size": 21},
        "point_label": {"font": FontID.SEASONS,     "size": 19},
    },
    {
        "id": "minimal_rosa", "name": "Min Rosa",
        "path": "backgrounds/minimalista-rosa.jpg", "color": "#fb868c",
        "title":       {"font": FontID.WEDGES,    "size": 76},
        "subtitle":    {"font": FontID.NOW_REGULAR, "size": 15},
        "symbol_size": 63,
        "sign_name":   {"font": FontID.NOW_REGULAR, "size": 25},
        "point_label": {"font": FontID.FUTURA,      "size": 18},
    },
]
