from config.db import base, engine
from pydantic import BaseModel

class UserSchema(BaseModel):
    id:int
    email:str
    hashed_password:str
    is_active: bool
    class Config:
        orm_mode = True
