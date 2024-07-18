from typing import Any

from async_lru import alru_cache
from open_meteo import OpenMeteo


class WeatherHTTPClient:
    @alru_cache
    async def get_weather_data(self, latitude: float, longitude: float) -> dict[Any, Any]:
        async with OpenMeteo() as open_meteo:
            forecast = await open_meteo.forecast(
                latitude=latitude,
                longitude=longitude,
                current_weather=True,
            )
            print(forecast.to_json())
            return forecast.to_dict()
