from fastapi import FastAPI, Path, Query
from typing import Optional, List
from pydantic import BaseModel

app = FastAPI(
    title="Fast API LMS",
    description="LMS for managing students and courses.",
    version="0.0.1",
    contact={
        "name": "Abhilash",
        "email": "abhilashchutia1999@gmail.com"
    },
    license_info={
        "name": "MIT"
    }
)

users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str] = None

@app.get("/")
async def read_root():
    return {"message":"Hello World"}

@app.get("/users", response_model=List[User])
async def get_users():
    return users

@app.post("/users")
async def create_users(user: User):
    users.append(user)
    return "Success"

@app.get("/users/{id}")
async def get_user(
    id: int = Path(..., description="The id of the user you want to retrive.", gt=2), 
    is_active: str = Query(None, max_length=5)):
    return users[id]