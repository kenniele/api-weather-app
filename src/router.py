from fastapi import APIRouter, Request, Form, Query
from fastapi.responses import HTMLResponse, JSONResponse
from geopy import Nominatim
from typing import List

from init import templates
from parse import get_weather

router_weather = APIRouter()


@router_weather.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "data": {"type": "response"}})


@router_weather.get("/{city}", response_class=HTMLResponse)
async def get_weather_by_city(request: Request, city: str):
    data = await get_weather(city)
    if data == {}:
        return templates.TemplateResponse("index.html", {"request": request, "city": city, "data": data})

    transl = {
        "Высота над уровнем моря": f'{data.get("elevation")} м.',
        "Температура": f'{data["current_weather"].get("temperature")}  C',
        "Скорость ветра": f'{data["current_weather"].get("wind_speed")} м/с',
    }
    return templates.TemplateResponse("index.html", {"request": request, "city": city, "data": data, "transl": transl})


@router_weather.post("/get_city")
async def get_city(request: Request, city: str = Form(...)):
    return {"redirect_url": f"/{city}"}


@router_weather.get("/autocomplete", response_class=JSONResponse)
async def autocomplete(query: str = Query(...)) -> List[str]:
    nominatim = Nominatim(user_agent="http")
    locations = nominatim.geocode(query, exactly_one=False, limit=5)
    if not locations:
        return []
    return [location.address for location in locations]
