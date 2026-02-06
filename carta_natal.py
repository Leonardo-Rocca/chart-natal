import swisseph as swe
from location import obtener_datos_ciudad, hora_utc
from chart_draw import draw_chart_artistic

BODIES = [
    (swe.SUN, "Sun"),
    (swe.MOON, "Moon"),
    (swe.MERCURY, "Mercury"),
    (swe.VENUS, "Venus"),
    (swe.MARS, "Mars"),
    (swe.JUPITER, "Jupiter"),
    (swe.SATURN, "Saturn"),
    (swe.URANUS, "Uranus"),
    (swe.NEPTUNE, "Neptune"),
    (swe.PLUTO, "Pluto"),
]

def generar_carta_final(nombre, ciudad, year, month, day, hour, minute, config_fondo):
    """
    Calcula las posiciones astronómicas y genera la imagen de la carta natal.
    Maneja la conversión UTC considerando cambios de fecha.
    """
    try:
        lat, lon, tz = obtener_datos_ciudad(ciudad)

        # Obtenemos la fecha y hora exacta en UTC (maneja saltos de día)
        y_u, m_u, d_u, h_u = hora_utc(year, month, day, hour, minute, tz)

        # Nota: julday acepta el año, mes, día y hora decimal en UTC
        jd = swe.julday(y_u, m_u, d_u, h_u)

        planets = {}
        for body_id, name in BODIES:
            # swe.calc devuelve (posiciones, flags) -> data[0] es la longitud eclíptica
            data, _ = swe.calc(jd, body_id)
            planets[name] = data[0]

        house_cusps, ascmc = swe.houses(jd, lat, lon, b'P')
        asc = ascmc[0]

        draw_chart_artistic(
            name=nombre,
            date_str=f"{day:02d} . {month:02d} . {year}",
            asc_deg=asc,
            house_cusps=house_cusps,
            planets=planets,
            bg_path=config_fondo["path"],
            color=config_fondo["color"]
        )

        print(f"✨ Carta generada exitosamente para {nombre} ({ciudad})")
        return True

    except Exception as e:
        print(f"Error en generar_carta_final: {e}")
        raise e

# --- BLOQUE DE PRUEBA (Opcional) ---
if __name__ == "__main__":
    # Esto solo se ejecuta si corres este archivo directamente,
    # no afectará cuando lo llames desde app.py
    generar_carta_final("Leo", "Buenos Aires, Argentina", 1994, 9, 19, 17, 30)