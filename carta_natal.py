import swisseph as swe
from location import obtener_datos_ciudad, hora_utc
from chart_draw import draw_chart_artistic

nombre = "Leo"
ciudad = "Buenos Aires, Argentina"

year, month, day = 1994, 9, 19
hour, minute = 17, 30

lat, lon, tz = obtener_datos_ciudad(ciudad)
hour_ut = hora_utc(year, month, day, hour, minute, tz)
jd = swe.julday(year, month, day, hour_ut)

# Planetas
planets = {}
for body, name in [
    (swe.SUN,"Sun"),
    (swe.MOON,"Moon"),
    (swe.MERCURY,"Mercury"),
    (swe.VENUS,"Venus"),
    (swe.MARS,"Mars"),
    (swe.JUPITER,"Jupiter"),
    (swe.SATURN,"Saturn"),
    (swe.URANUS,"Uranus"),
    (swe.NEPTUNE,"Neptune"),
    (swe.PLUTO,"Pluto"),
]:
    data,_ = swe.calc(jd, body)
    planets[name] = data[0]


# Casas Placidus
house_cusps, ascmc = swe.houses(jd, lat, lon, b'P')
asc = ascmc[0]

draw_chart_artistic(
    name=nombre,
    date_str=f"{day}/{month}/{year}",
    asc_deg=asc,
    house_cusps=house_cusps,
    planets=planets
)

print("Imagen generada: carta_natal.png")
