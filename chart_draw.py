import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib import font_manager as fm
from types_config import Fondo

SYMBOLS_NAME_FONT_PATH = "fonts/DancingScript-VariableFont_wght.ttf"

ZODIAC_SIGNS = ["♈","♉","♊","♋","♌","♍","♎","♏","♐","♑","♒","♓"]
PLANET_SYMBOLS = {
    "Sun": "☉",
    "Moon": "☽",
    "Mercury": "☿",
    "Venus": "♀",
    "Mars": "♂",
    "Jupiter": "♃",
    "Saturn": "♄",
    "Uranus": "♅",
    "Neptune": "♆",
    "Pluto": "♇"
}

# ============================
# Constantes de radios / layout
# ============================
# Todos los radios están en la escala [0, 1] de matplotlib polar.

# Radios base para anillos y líneas
RADIUS_ASPECT_LINES   = 0.38   # donde se dibujan los aspectos (líneas entre planetas)
RADIUS_HOUSES_CIRCLE  = 0.78   # círculo exterior de la zona de casas / planetas
RADIUS_PLANETS_ORBIT  = 0.85   # órbita visual de planetas si hicieran un anillo propio (reservado)
RADIUS_SIGNS_CIRCLE   = 0.98   # círculo exterior de los signos

# Anillo de cúspides: reutiliza el mismo radio que los aspectos para mantener centro limpio
RADIUS_CUSP_RING      = RADIUS_ASPECT_LINES

# Nuevo anillo interno para numerar casas (entre cúspides y círculo de casas)
RADIUS_HOUSE_NUMBERS_RING = 0.50
HOUSE_NUMBER_INNER_OFFSET = 0.04  # cuánto se meten los números hacia el interior del anillo

# ============================
# PLANETAS (zona ampliada)
# ============================
RADIUS_PLANETS_INNER  = 0.62
RADIUS_PLANETS_OUTER  = 0.82
RADIUS_PLANET_SYMBOLS = 0.72   # centro del anillo planetario

# ============================
# Signos
# ============================
RADIUS_SIGNS_CIRCLE = 0.95
SIGN_LABEL_OFFSET  = 0.08
RADIUS_SIGN_LABELS = RADIUS_SIGNS_CIRCLE - SIGN_LABEL_OFFSET

# Configuración de aspectos (en grados)
ASPECT_ANGLES_DEG = {
    "conjunction": 0,
    "sextile": 60,
    "square": 90,      # cuadratura
    "trine": 120,
    "opposition": 180,
}

# Orbes (en grados)
ASPECT_ORB_GENERAL_DEG    = 5   # orbe para todos los aspectos en general
ASPECT_ORB_LUMINARIES_DEG = 10  # orbe especial cuando intervienen Sol o Luna

def signo_zodiacal(grados):
    index = int(grados // 30)  # división entera
    return ZODIAC_SIGNS[index]

def get_sign_name(degrees):
    nombres_signos = [
        "Aries", "Tauro", "Géminis", "Cáncer",
        "Leo", "Virgo", "Libra", "Escorpio",
        "Sagitario", "Capricornio", "Acuario", "Piscis"
    ]
    # Dividimos los 360° en 12 partes de 30° cada una
    indice = int((degrees % 360) / 30)
    return nombres_signos[indice]

def mid_angle(a1, a2):
    """Punto medio angular correcto (maneja wrap 360°)"""
    diff = (a2 - a1) % 360
    return (a1 + diff / 2) % 360

def astro_angle(deg, asc):
    """
    Convierte grados zodiacales a ángulo matplotlib,
    usando la misma convención que para signos y planetas:
    se resta el ASC para que éste quede en el oeste (izquierda).
    """
    return np.deg2rad((deg - asc) % 360)


def draw_chart_artistic(
    name: str,
    date_str: str,
    asc_deg: float,
    house_cusps: list,
    planets: dict,
    config_fondo: Fondo, # Reemplaza bg_path y color
    out_path: str = "carta_natal.png"
):
    color = config_fondo["color"]
    bg_path = config_fondo["path"]
    name_font_path = config_fondo["name_font"]
    subname_font_path = config_fondo["subname_font"]

    fig = plt.figure(figsize=(8.27, 11.69))  # A4 vertical
    ax = plt.subplot(111, polar=True)
    ax.set_position([0.11, 0.11, 0.78, 0.78])
    ax.set_ylim(0,1)
    ax.axis("off")
    ax.set_theta_zero_location("W")
    ax.set_theta_direction(1)

    ax_bottom = fig.add_axes([0, -0.05, 1, 0.15])  # ocupa solo la parte inferior
    ax_bottom.axis("off")

    offset = np.deg2rad(asc_deg)


    # Fondo
    bg = Image.open(bg_path).convert("RGBA")
    bg = bg.resize(
        (int(fig.get_figwidth()*300),
         int(fig.get_figheight()*300))
    )
    fig.figimage(bg, xo=0, yo=0, zorder=-10)

    # Radios (definidos como constantes al inicio del archivo)

    # Dibujamos:
    # - anillo interno para números de casas
    # - anillo exterior de casas / planetas
    # - anillo exterior de signos
    for r in [RADIUS_HOUSE_NUMBERS_RING, RADIUS_HOUSES_CIRCLE, RADIUS_SIGNS_CIRCLE]:
        ax.plot(np.linspace(0, 2*np.pi, 360), [r]*360,
                color=color, lw=1.5, alpha=0.8)


    # Casas (NO llegan al centro)
    for cusp in house_cusps:
        theta = np.deg2rad(cusp) - offset
        ax.plot([theta, theta], [RADIUS_ASPECT_LINES, RADIUS_HOUSES_CIRCLE],
                color=color, lw=1.0)

    # Signos
    for i, sign in enumerate(ZODIAC_SIGNS):
        angle = np.deg2rad(i * 30 + 15) - offset
        ax.text(angle, RADIUS_SIGN_LABELS, sign,
                color=color, fontsize=20,
                ha="center", va="center")

        # líneas divisorias de signos
        div = np.deg2rad(i * 30) - offset
        ax.plot([div, div], [RADIUS_HOUSES_CIRCLE, RADIUS_SIGNS_CIRCLE],
                color=color, lw=1.5, alpha=0.9)

    # Planetas
    for name_p, lon in planets.items():
        theta = np.deg2rad(lon) - offset
        symbol = PLANET_SYMBOLS.get(name_p, "●")

        ax.text(
            theta,
            RADIUS_PLANET_SYMBOLS, # offset radial para símbolos de planetas
            symbol,
            color=color,
            fontsize=17,
            ha="center",
            va="center"
        )

    # aro final
    ax.plot(
        np.linspace(0, 2*np.pi, 360),
        [RADIUS_CUSP_RING] * 360,
        color=color,
        lw=0.8,
        alpha=0.9
    )

    # =========================
    # Números de casas (I–XII)
    # =========================
    # Se colocan un poco dentro del anillo interno de casas
    r_house_numbers = RADIUS_HOUSE_NUMBERS_RING - HOUSE_NUMBER_INNER_OFFSET
    for i in range(12):
        cusp_start = house_cusps[i]
        cusp_end   = house_cusps[(i + 1) % 12]

        mid = mid_angle(cusp_start, cusp_end)
        theta = np.deg2rad(mid) - offset

        ax.text(
            theta,
            r_house_numbers,
            str(i + 1),
            color=color,
            fontsize=8,
            ha="center",
            va="center"
        )


    # Aspectos (centro limpio)
    aspect_angles = list(ASPECT_ANGLES_DEG.values())
    plist = list(planets.items())

    for i in range(len(plist)):
        for j in range(i+1, len(plist)):
            name_i, lon_i = plist[i]
            name_j, lon_j = plist[j]

            d = abs((lon_i - lon_j + 180) % 360 - 180)

            # Orbe más amplio si intervienen Sol o Luna
            orb = ASPECT_ORB_LUMINARIES_DEG if (
                name_i in ("Sun", "Moon") or name_j in ("Sun", "Moon")
            ) else ASPECT_ORB_GENERAL_DEG

            if any(abs(d - a) <= orb for a in aspect_angles):
                t1 = astro_angle(lon_i, asc_deg)
                t2 = astro_angle(lon_j, asc_deg)
                # Las líneas de aspecto se dibujan en el anillo interno de aspectos
                ax.plot([t1, t2], [RADIUS_HOUSE_NUMBERS_RING, RADIUS_HOUSE_NUMBERS_RING],
                        color=color, lw=2.5, alpha=0.6)

    # ===================================
    # Nombre con fuente personalizada
    # ===================================

    name_font = fm.FontProperties(fname=name_font_path, size=80)

    fig.text(
        0.5, 0.87,
        name,
        ha="center",
        fontproperties=name_font,
        color=color
    )
    fig.text(
        0.5, 0.83,
        date_str,
        ha="center",
        fontproperties=fm.FontProperties(fname=subname_font_path, size=15),
        color=color
    )


    draw_special_points(
        ax=ax_bottom,
        asc_deg=asc_deg,
        planets=planets,
        color=color,
        name_font_path=name_font_path,
        subname_font_path=subname_font_path,
    )


    plt.savefig(out_path, dpi=300)
    plt.close()



def draw_special_points(ax, asc_deg, planets, color,name_font_path, subname_font_path, spacing=0.28, y_pos=0.9):
    # Diccionario para mapear los nombres técnicos a los textos decorativos de la imagen
    display_names = {
        "Sol": "Signo\nSolar",
        "Luna": "Signo\nLunar",
        "Asc": "Signo\nAscendente"
    }

    special_points = [
        ("Sol", signo_zodiacal(planets["Sun"]), get_sign_name(planets["Sun"])),
        ("Luna", signo_zodiacal(planets["Moon"]), get_sign_name(planets["Moon"])),
        ("Asc", signo_zodiacal(asc_deg), get_sign_name(asc_deg))
    ]

    n = len(special_points)
    fontsize = 45

    for i, (key, symbol, sign_name) in enumerate(special_points):
        # Calculamos el centro de cada grupo
        x_center = spacing*(n-1)/2 + i*spacing - 0.10

        # 1. DIBUJAR EL SÍMBOLO (Lado Derecho)
        ax.text(
            x_center + 0.05, y_pos - 0.2,
            symbol,
            ha="left", va="bottom",
            color=color, fontsize=fontsize * 1.4,
            transform=ax.transAxes
        )

        # 2. DIBUJAR "Signo Solar/Lunar/etc" (Arriba Izquierda)
        ax.text(
            x_center + 0.04, y_pos,
            display_names[key],
            ha="right", va="bottom",
            color=color,
            linespacing=0.8,
            fontproperties=fm.FontProperties(fname=name_font_path, size=fontsize * 0.7),
            transform=ax.transAxes
        )


        # 3. DIBUJAR EL NOMBRE DEL SIGNO (Abajo Izquierda - Ej: "Virgo")
        ax.text(
            x_center, y_pos,
            sign_name,
            ha="center", va="top",
            color=color,
            fontproperties=fm.FontProperties(fname=subname_font_path, size=fontsize * 0.3),
            transform=ax.transAxes
        )