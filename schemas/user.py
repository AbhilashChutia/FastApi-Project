from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    email: str
    role: int

class UserCreate(UserBase):
    ...

class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True