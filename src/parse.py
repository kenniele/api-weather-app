from geopy import Nominatim

from init import weather_client


async def get_weather(city: str) -> dict:
    nominatim = Nominatim(user_agent="http")
    location = nominatim.geocode(city)
    if location is None:
        return {}
    latitude = location.latitude
    longitude = location.longitude
    data = await weather_client.get_weather_data(latitude, longitude)
    return data
