from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
from timezonefinder import TimezoneFinder
import pytz
from datetime import datetime

def get_city_data(city, max_retries=3, timeout=10):
    """Returns (lat, lon, tz) for a city."""

    # Special case: Buenos Aires
    if city.strip().lower() == "buenos aires, argentina":
        lat, lon = -34.6095579, -58.3887904
        tf = TimezoneFinder()
        timezone_str = tf.timezone_at(lat=lat, lng=lon)
        return lat, lon, pytz.timezone(timezone_str)

    geolocator = Nominatim(user_agent="carta-natal-app", timeout=timeout)

    for _ in range(max_retries):
        try:
            location = geolocator.geocode(city)
            if location:
                lat, lon = location.latitude, location.longitude
                tf = TimezoneFinder()
                timezone_str = tf.timezone_at(lat=lat, lng=lon)
                if not timezone_str:
                    raise ValueError("Could not determine timezone")
                return lat, lon, pytz.timezone(timezone_str)
            break
        except (GeocoderTimedOut, GeocoderServiceError):
            continue

    raise ValueError(f"Could not find city: {city}")

def to_utc(year, month, day, hour, minute, tz):
    """
    Converts local time to UTC, returning year, month, day and decimal hour.
    Critical for births near midnight.
    """
    local_dt = tz.localize(datetime(year, month, day, hour, minute))
    utc_dt = local_dt.astimezone(pytz.utc)

    year_utc = utc_dt.year
    month_utc = utc_dt.month
    day_utc = utc_dt.day
    hour_utc = utc_dt.hour + utc_dt.minute / 60.0 + utc_dt.second / 3600.0

    return year_utc, month_utc, day_utc, hour_utc