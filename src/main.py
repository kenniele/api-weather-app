from fastapi import FastAPI, applications
from fastapi.openapi.docs import get_swagger_ui_html
from starlette.staticfiles import StaticFiles

import uvicorn

from router import router_weather


def swagger_monkey_patch(*args, **kwargs):
    return get_swagger_ui_html(
        *args, **kwargs,
        swagger_js_url="https://cdn.staticfile.net/swagger-ui/5.1.0/swagger-ui-bundle.min.js",
        swagger_css_url="https://cdn.staticfile.net/swagger-ui/5.1.0/swagger-ui.min.css")


applications.get_swagger_ui_html = swagger_monkey_patch
app = FastAPI(reload=True, title="Weather API")


app.include_router(router_weather)

app.mount("/static", StaticFiles(directory="../static/"), name="static")

origins = [
    "http://localhost",
    "http://127.0.0.1"
]

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="127.0.0.1", reload=True)
