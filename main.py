from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import subprocess

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
  return templates.TemplateResponse("index.html", {"request": request})

@app.get("/webhook")
async def webhook():
    subprocess.call("/home/tomoki/bin/oichiku-deploy")
