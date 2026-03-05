from enum import Enum
from typing import TypedDict, Dict, List

# 1. Definimos el "Símbolo" (Enum)
class FontID(Enum):
    MOON_TIME_REGULAR = "fonts/MoonTime-Regular-1.ttf"
    NOW_REGULAR = "fonts/Now-Regular.otf"
    FUTURA = "fonts/FuturaCyrillicLight.ttf"
    NIXIE_ONE = "fonts/NixieOne.ttf"
    SEASONS = "fonts/The Seasons Regular.ttf"
    WEDGES = "fonts/Wedges.ttf"

# 2. Definimos el Mapa de Estilos (Tamaños fijos por fuente)
# Estructura: (tamaño_nombre, tamaño_subnombre, tamaño_simbolo)
FONT_STYLES: Dict[FontID, Dict[str, int]] = {
    FontID.MOON_TIME_REGULAR: {
        "title": 78,
        "subtitle": 1,
        "symbol": 50
    },
    FontID.NOW_REGULAR: {
        "title": 76,
        "subtitle": 15,
        "symbol": 45
    },
    FontID.FUTURA: {
        "title": 76,
        "subtitle": 1,
        "symbol": 45
    },
    FontID.NIXIE_ONE: {
        "title": 76,
        "subtitle": 15,
        "symbol": 45
    },
    FontID.SEASONS: {
        "title": 76,
        "subtitle": 1,
        "symbol": 35
    },
    FontID.WEDGES: {
        "title": 76,
        "subtitle": 1,
        "symbol": 45
    }
}

class Background(TypedDict):
    id: str
    name: str
    path: str
    color: str
    name_font: FontID
    subname_font: FontID



BACKGROUNDS: List[Background] = [
    {"id": "noche_estrellada", "name": "Noche del Lobo", "path": "backgrounds/background.jpg", "color": "white",
        "name_font": FontID.MOON_TIME_REGULAR, "subname_font": FontID.NOW_REGULAR},
    {"id": "nebulosa", "name": "Nebulosa", "path": "backgrounds/background2.jpg", "color": "white",
        "name_font": FontID.MOON_TIME_REGULAR, "subname_font": FontID.NOW_REGULAR},
    {"id": "minimal_rosa", "name": "Minimalista rosa", "path": "backgrounds/minimalista-rosa.jpg", "color": "#fb868c",
        "name_font": FontID.FUTURA, "subname_font": FontID.NOW_REGULAR},
    {"id": "negro", "name": "Negro", "path": "backgrounds/black.jpg", "color": "white",
        "name_font": FontID.MOON_TIME_REGULAR, "subname_font": FontID.NOW_REGULAR},
    {"id": "verde", "name": "Verde", "path": "backgrounds/green.jpg", "color": "white",
        "name_font": FontID.FUTURA, "subname_font": FontID.NOW_REGULAR},
    {"id": "azul_estrella", "name": "Azul estrella", "path": "backgrounds/blue-stars.jpg", "color": "white",
        "name_font": FontID.FUTURA, "subname_font": FontID.NIXIE_ONE},
    {"id": "gold", "name": "Gold", "path": "backgrounds/gold.jpg", "color": "#d4b68e",
        "name_font": FontID.MOON_TIME_REGULAR, "subname_font": FontID.NOW_REGULAR},
    {"id": "beige", "name": "Beige", "path": "backgrounds/beige.jpg", "color": "#805010",
        "name_font": FontID.SEASONS, "subname_font": FontID.NOW_REGULAR},
]