import swisseph as swe
from location import get_city_data, to_utc
from chart_draw import draw_chart_artistic, DEFAULT_LANGUAGE
from config import Background


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

def generate_final_chart(
    name: str,
    city: str,
    year: int,
    month: int,
    day: int,
    hour: int,
    minute: int,
    background_config: Background,
    language: str = DEFAULT_LANGUAGE
) -> bool:
    """
    Calculates astronomical positions and generates the natal chart image.
    Handles UTC conversion including date changes.
    """
    try:
        lat, lon, tz = get_city_data(city)

        year_utc, month_utc, day_utc, hour_utc = to_utc(year, month, day, hour, minute, tz)

        jd = swe.julday(year_utc, month_utc, day_utc, hour_utc)

        planets = {}
        for body_id, body_name in BODIES:
            data, _ = swe.calc(jd, body_id)
            planets[body_name] = data[0]

        house_cusps, ascmc = swe.houses(jd, lat, lon, b'P')
        asc = ascmc[0]

        draw_chart_artistic(
            name=name,
            date_str=f"{day:02d} . {month:02d} . {year}",
            asc_deg=asc,
            house_cusps=house_cusps,
            planets=planets,
            background_config=background_config,
            language=language
        )

        print(f"✨ Chart generated successfully for {name} ({city})")
        return True

    except Exception as e:
        print(f"Error in generate_final_chart: {e}")
        raise e

if __name__ == "__main__":
    generate_final_chart("Leo", "Buenos Aires, Argentina", 1994, 9, 19, 17, 30)