from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(tags=["Users"])

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [User(id=1, name="elias", surname="Bliss", url="www.elias.com", age=29 ),
        User(id=2, name="joel", surname="Bunny", url="www.joel.com", age=22)]

@router.get("/users/", response_model=list[User])
async def users():
    """
    Lista a todos los usuarios
    """
    return users_list

# Path
@router.get("/user/{id}", response_model=User)
async def user(id: int):
    """
    Busca usuario por Id
    """
    return search_user(id)

# Query
@router.get("/user/", response_model=User)
async def user(surname: str):
    """
    Busca usuario por surname
    """
    users = filter(lambda user: user.surname == surname, users_list)
    
    try:
        return list(users)[0]
    except: 
        raise HTTPException(status_code=404, detail="usuario no existe")

@router.post("/user/", response_model=User, status_code=201)
async def user(user: User):
    """
    Crea un nuevo usuario
    """
    if type(search_user(user.id)) is User:
        raise HTTPException(status_code=404, detail="Usuario ya existe")
    users_list.append(user)

    return user

@router.put("/user/", response_model=User)
async def user(user: User):
    """
    Actualiza un usuario por el ID
    """
    found = False

    for index, update_user in enumerate(users_list):
        if update_user.id == user.id:
            users_list[index] = user
            found = True
    
    if not found:
        raise HTTPException(status_code=404, detail="no se pudo actualizar el usuario")

    return user

@router.delete("/user/{id}")
async def user(id: int):
    """
    Elimina un usuario por el ID
    """
    found = False
    for index, delete_user in enumerate(users_list):
        if delete_user.id == id:
            users_list[index] = user
            found = True

    if not found:
        return {"error": "no se pudo eliminar el usuario"}
    

# util
def search_user(id: int):
    """
    Busca Un usuario por el ID
    """
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        raise HTTPException(status_code=404, detail="usuario no existe")