from typing import Union
from fastapi import APIRouter, Depends
from config.db import engine, sessionLocal
from sqlalchemy.orm import Session
from schemas.user_schemas import UserSchema

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

UserRouter = APIRouter()

@UserRouter.get("/")
def read_user():
    return {"Hello": "World"}


@UserRouter.post("/")
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = UserSchema(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user