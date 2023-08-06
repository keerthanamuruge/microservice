from sqlalchemy import Boolean, Column, Integer, String
from config.db import base, engine

class User(base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    base.metadata.create_all(bind=engine)
    