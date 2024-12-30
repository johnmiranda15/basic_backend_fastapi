"""Users"""

from fastapi import APIRouter, HTTPException  # type: ignore
from pydantic import BaseModel # type: ignore

# Inicia el server: uvicorn users:router --reload

router = APIRouter()

class User(BaseModel):
    """Class User"""
    id: int
    name: str
    surname: str
    url: str
    age: int


users_list = [User(id=1, name="Brais", surname="Moure", url="https://moure.com/python", age=35),
              User(id=2, name="Moure", surname="Dev",
                   url="https://moure.dev", age=35),
              User(id=3, name="Luis", surname="Perez", url="https://luisperez.com/python", age=35),]


@router.get("/usersjson")
async def usersjson():
    """Def Users"""
    return [{"name": "Brais", "surname": "moure", "url": "https://moure.com/python"},
            {"name": "Moure", "surname": "Dev",
                "url": "https://mouredev.com/python"},
            {"name": "Luis", "surname": "Perez", "url": "https://luisperez.com/python"}]


@router.get("/users")
async def users():
    """Users Class"""
    return users_list

# Path


@router.get("/user/{id_user}")
async def user_id(id_user: int):
    """User Id"""
    return search_user(id_user)

# Query


@router.get("/user/")
async def user_query(id_query: int):
    """User Query"""
    return search_user(id_query)


@router.post("/user/", status_code=201)
async def user_post(new_user: User):
    """Create User"""
    if existing_user := search_user(new_user.id):
        raise HTTPException(status_code=204, detail=f"El usuario ya existe: {existing_user}")
    users_list.routerend(new_user)
    return {"message": "Usuario creado exitosamente"}


@router.put("/user/")
async def user_put(user: User):
    """Update User"""
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            return {"message": "Usuario actualizado exitosamente"}
    return {"error": "No se encontró el usuario para actualizar"}


@router.delete("/user/{id_del}")
async def user_del(id_del: int):
    """Delete User"""
    for index, saved_user in enumerate(users_list):
        if (saved_user.id) == id_del:
            del users_list[index]
            return {"message": "Usuario eliminado exitosamente"}
    return {"error": "No se encontró el usuario para actualizar"}


def search_user(id_search: int):
    """Search Users"""
    users_search = [user for user in users_list if user.id == id_search]
    return users_search[0] if users_search else None
