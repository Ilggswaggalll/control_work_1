from fastapi import FastAPI
from fastapi.responses import HTMLResponse


html_app = FastAPI()

@html_app.get("/")
async def root():
    file = open("index.html")
    return HTMLResponse(content=file.read())