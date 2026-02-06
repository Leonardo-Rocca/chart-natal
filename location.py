from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
from timezonefinder import TimezoneFinder
import pytz
from datetime import datetime

def obtener_datos_ciudad(ciudad, max_retries=3, timeout=10):
    """
    Devuelve (lat, lon, tz) para una ciudad.
    Incluye reintentos y timeout configurable para el servicio de geocodificación.
    """

    # Caso especial: evitar llamada al geolocator para Buenos Aires
    if ciudad.strip().lower() == "buenos aires, argentina":
        lat = -34.6095579
        lon = -58.3887904

        tf = TimezoneFinder()
        timezone_str = tf.timezone_at(lat=lat, lng=lon)

        if not timezone_str:
            raise ValueError("No se pudo determinar la zona horaria")

        tz = pytz.timezone(timezone_str)
        return lat, lon, tz

    geolocator = Nominatim(user_agent="carta-natal-app", timeout=timeout)

    last_exception = None
    for _ in range(max_retries):
        try:
            location = geolocator.geocode(ciudad)
            break
        except GeocoderTimedOut as exc:
            last_exception = exc
            continue
        except GeocoderServiceError as exc:
            raise RuntimeError(f"Error del servicio de geocodificación: {exc}")
    else:
        # Solo se ejecuta si el bucle termina sin hacer break
        raise RuntimeError("Geocoder timeout tras varios intentos. Intente nuevamente.")

    if not location:
        raise ValueError("Ciudad no encontrada")

    lat = location.latitude
    lon = location.longitude

    tf = TimezoneFinder()
    timezone_str = tf.timezone_at(lat=lat, lng=lon)

    if not timezone_str:
        raise ValueError("No se pudo determinar la zona horaria")

    tz = pytz.timezone(timezone_str)

    return lat, lon, tz

def hora_utc(year, month, day, hour, minute, tz):
    local_dt = tz.localize(
        datetime(year, month, day, hour, minute)
    )
    utc_dt = local_dt.astimezone(pytz.utc)

    # =========================
    # INPUTS
    # =========================
    nombre = "Leo"#input("Nombre: ")
    ciudad = "Buenos Aires, Argentina" #//input("Ciudad y país (ej: Buenos Aires, Argentina): ")

    year = 1994#int(input("Año (YYYY): "))
    month = 9#int(input("Mes (1-12): "))
    day = 19#int(input("Día (1-31): "))

    hour = 17#int(input("Hora (0-23): "))
    minute = 30#int(input("Minutos (0-59): "))

    return utc_dt.hour + utc_dt.minute / 60
