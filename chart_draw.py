import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

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

def mid_angle(a1, a2):
    """Punto medio angular correcto (maneja wrap 360°)"""
    diff = (a2 - a1) % 360
    return (a1 + diff / 2) % 360

def astro_angle(deg, asc):
    """
    Convierte grados zodiacales a ángulo matplotlib,
    corrigiendo espejo y rotando por ASC
    """
    return np.deg2rad((180 - (deg - asc)) % 360)

def draw_chart_artistic(
    name,
    date_str,
    asc_deg,
    house_cusps,
    planets,
    bg_path="background.jpg",
    out_path="carta_natal.png"
):

    fig = plt.figure(figsize=(8.27, 11.69))  # A4 vertical
    ax = plt.subplot(111, polar=True)
    ax.set_position([0.1, 0.12, 0.8, 0.8])
    ax.set_ylim(0,1)
    ax.axis("off")
    ax.set_theta_zero_location("W")
    ax.set_theta_direction(1)

    offset = np.deg2rad(asc_deg)


    # Fondo
    bg = Image.open(bg_path).convert("RGBA")
    bg = bg.resize(
        (int(fig.get_figwidth()*300),
         int(fig.get_figheight()*300))
    )
    fig.figimage(bg, xo=0, yo=0, zorder=-10)

    # Radios
    r_aspects = 0.50
    r_houses  = 0.75
    r_planets = 0.85
    r_signs   = 0.95
    r_cusp_ring = 0.50
    r_planets_offset = 0.70


    for r in [r_houses, r_signs]:
        ax.plot(np.linspace(0, 2*np.pi, 360), [r]*360,
                color="white", lw=0.8, alpha=0.8)

    # Casas (NO llegan al centro)
    for cusp in house_cusps:
        theta = np.deg2rad(cusp) - offset
        ax.plot([theta, theta], [r_aspects, r_houses],
                color="white", lw=0.7)

    # Signos
    for i, sign in enumerate(ZODIAC_SIGNS):
        angle = np.deg2rad(i * 30 + 15) - offset
        ax.text(angle, r_signs - 0.08, sign,
                color="white", fontsize=28,
                ha="center", va="center")

        # líneas divisorias de signos
        div = np.deg2rad(i * 30) - offset
        ax.plot([div, div], [r_houses, r_signs],
                color="white", lw=0.5, alpha=0.6)

    # Planetas
    for name_p, lon in planets.items():
        theta = np.deg2rad(lon) - offset
        symbol = PLANET_SYMBOLS.get(name_p, "●")

        ax.text(
            theta,
            r_planets_offset, #offset agregado por leo
            symbol,
            color="white",
            fontsize=16,
            ha="center",
            va="center"
        )

    # aro final
    ax.plot(
        np.linspace(0, 2*np.pi, 360),
        [r_cusp_ring] * 360,
        color="white",
        lw=0.8,
        alpha=0.9
    )

    # =========================
    # Números de casas (I–XII)
    # =========================
    r_house_numbers = (r_cusp_ring + r_houses) / 2
    for i in range(12):
        cusp_start = house_cusps[i]
        cusp_end   = house_cusps[(i + 1) % 12]

        mid = mid_angle(cusp_start, cusp_end)
        theta = np.deg2rad(mid) - offset

        ax.text(
            theta,
            r_house_numbers,
            str(i + 1),
            color="white",
            fontsize=12,
            ha="center",
            va="center"
        )


    # Aspectos (centro limpio)
    aspects = [0,60,90,120,180]
    plist = list(planets.items())

    for i in range(len(plist)):
        for j in range(i+1, len(plist)):
            d = abs((plist[i][1]-plist[j][1]+180)%360-180)
            if any(abs(d-a)<=4 for a in aspects):
                t1 = astro_angle(plist[i][1], asc_deg)
                t2 = astro_angle(plist[j][1], asc_deg)
                ax.plot([t1,t2],[r_aspects,r_aspects],
                        color="white", lw=0.6, alpha=0.6)

    # Texto
    fig.text(0.5,0.93,name,ha="center",
             fontsize=20,color="white")
    fig.text(0.5,0.90,date_str,ha="center",
             fontsize=11,color="white")

    plt.savefig(out_path, dpi=300)
    plt.close()
