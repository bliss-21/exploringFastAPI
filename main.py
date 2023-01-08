from fastapi import FastAPI, Request
from routers import users, products
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Templates Html
templates = Jinja2Templates(directory="templates")

# Routers
app.include_router(users.router)
app.include_router(products.router)

# Recursos staticos
app.mount("/static", StaticFiles(directory="static"), name="static")
# http://127.0.0.1:8000/static/path/file.ext

# Url local: http://127.0.0.1:8000

@app.get("/")
def home(request:Request):
    return templates.TemplateResponse("home.html",{"request":request})
