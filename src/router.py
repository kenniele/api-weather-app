from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse

from init import templates
from parse import get_weather

import database

router_weather = APIRouter()


@router_weather.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    ip = request.client.host
    await database.add_user(ip)
    last = await database.last_city(ip)
    return templates.TemplateResponse(request, "index.html", {"data": "response", "last": last})


@router_weather.get("/{city}", response_class=HTMLResponse)
async def get_weather_by_city(request: Request, city: str):
    data = await get_weather(city)
    if data == {}:
        return templates.TemplateResponse(request, "index.html", {"city": city, "data": data})

    ip = request.client.host
    await database.set_history(ip, city)
    await database.add_stat(city)
    count = await database.get_stat(city)

    transl = {
        "Высота над ур. моря": f'{data.get("elevation")} м.',
        "Температура": f'{data["current_weather"].get("temperature")}  °C',
        "Скорость ветра": f'{data["current_weather"].get("wind_speed")} м/с',
        "Этот адрес запрашивали": f"{count} р.",
    }
    return templates.TemplateResponse(request, "index.html", {"city": city, "data": data, "transl": transl})


@router_weather.get("/info/{city}", response_class=JSONResponse)
async def get_info(request: Request, city: str):
    count = await database.get_stat(city)
    return {"city": city, "count": count}


@router_weather.post("/get_city")
async def get_city(request: Request, city: str = Form(...)):
    return {"redirect_url": f"/{city}"}
