from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
from timezonefinder import TimezoneFinder
import pytz
from datetime import datetime

def obtener_datos_ciudad(ciudad, max_retries=3, timeout=10):
    """Devuelve (lat, lon, tz) para una ciudad."""

    # Caso especial: Buenos Aires
    if ciudad.strip().lower() == "buenos aires, argentina":
        lat, lon = -34.6095579, -58.3887904
        tf = TimezoneFinder()
        timezone_str = tf.timezone_at(lat=lat, lng=lon)
        return lat, lon, pytz.timezone(timezone_str)

    geolocator = Nominatim(user_agent="carta-natal-app", timeout=timeout)

    for _ in range(max_retries):
        try:
            location = geolocator.geocode(ciudad)
            if location:
                lat, lon = location.latitude, location.longitude
                tf = TimezoneFinder()
                timezone_str = tf.timezone_at(lat=lat, lng=lon)
                if not timezone_str:
                    raise ValueError("No se pudo determinar la zona horaria")
                return lat, lon, pytz.timezone(timezone_str)
            break
        except (GeocoderTimedOut, GeocoderServiceError):
            continue

    raise ValueError(f"No se pudo encontrar la ciudad: {ciudad}")

def hora_utc(year, month, day, hour, minute, tz):
    """
    Convierte hora local a UTC devolviendo año, mes, día y hora decimal.
    Esto es CRUCIAL para nacimientos cerca de la medianoche (como el caso de Lima).
    """
    # 1. Crear objeto datetime local
    local_dt = tz.localize(datetime(year, month, day, hour, minute))

    # 2. Convertir a UTC
    utc_dt = local_dt.astimezone(pytz.utc)

    # 3. Retornar los 4 componentes necesarios para swisseph
    y_u = utc_dt.year
    m_u = utc_dt.month
    d_u = utc_dt.day
    h_u = utc_dt.hour + utc_dt.minute / 60.0 + utc_dt.second / 3600.0

    return y_u, m_u, d_u, h_u