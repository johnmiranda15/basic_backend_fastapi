"""auth"""

from fastapi import APIRouter, HTTPException, Depends  # type: ignore
from pydantic import BaseModel # type: ignore
from fastapi.security import OAuth2PasswordBearer, OAuthPasswordRequestForm # type: ignore

# Inicia el server: uvicorn users:router --reload

router = APIRouter()
oauth2 = OAuth2PasswordBearer(tokenUrl="login")



class User(BaseModel):
    """Class Auth User"""
    username: str
    full_name: str
    email: str
    disabled: bool

class UserDB(User):
    """Class Auth User DB"""
    pasword: str

users_db = {
    "jaunq:": {
        "username": "jaunq",
        "full_name": "Juan Quintero",
        "email": "mirandajohn634@gmailcom",
        "pasword": "1234",
        "disabled": False
    },
    "jose:": {
        "username": "jose",
        "full_name": "Jose Perez",
        "email": "jose@gmailcom",
        "pasword": "1234",
        "disabled": True
    }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
}

def search_user(username: str):
    """Search User"""
    if username in users_db:
        return users_db[username]
    return None 

@router.post("/login")
async def login(form_data: OAuthPasswordRequestForm = Depends()):
    user_dict = users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Usuario no encontrado")
    user = UserDB(**user_dict)
    if form_data.password != user.password:
        raise HTTPException(status_code=400, detail="Contraseña incorrecta")
    return {"access_token": user.username, "token_type": "bearer"}