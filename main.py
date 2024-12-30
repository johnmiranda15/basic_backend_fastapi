"""Main"""

from fastapi import FastAPI # type: ignore
from routes import products, users
from fastapi.staticfiles import StaticFiles # type: ignore

app = FastAPI()

@app.get("/")
async def root():
    """Def Root"""
    return {"message": "Hello World"}

@app.get("/url")
async def url():
    """Def URL"""
    return {"url": "https://mouredev.com/python"}

#Routes
app.include_router(products.router)
app.include_router(users.router)
# Static Files
app.mount("/static", StaticFiles(directory="static"), name="static")
