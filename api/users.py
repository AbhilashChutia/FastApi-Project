import fastapi
from fastapi import Depends, HTTPException
from typing import Optional, List
from sqlalchemy.orm import Session

from db.db_setup import get_db
from schemas.user import User, UserCreate
from api.utils.users import get_user, get_user_by_email, get_users, create_user

router = fastapi.APIRouter()

@router.get("/users", response_model=List[User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users

@router.post("/users", response_model=User, status_code=201)
async def create_new_users(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)

@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user