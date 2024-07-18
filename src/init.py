from http_client import WeatherHTTPClient
from fastapi.templating import Jinja2Templates

weather_client = WeatherHTTPClient()

templates = Jinja2Templates(directory="../templates")
