"""main"""

from fastapi import FastAPI # type: ignore
from routes import products, users, basic_auth_users
from fastapi.staticfiles import StaticFiles # type: ignore

app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(users.router)
app.include_router(basic_auth_users.router)

# Static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return "Hola FastAPI!"

@app.get("/url")
async def url():
    return {"url": "https://mouredev.com/python"}
