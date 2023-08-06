from typing import Union

from fastapi import FastAPI
from apis.user import UserRouter

app = FastAPI()
app.include_router(UserRouter, prefix="/users")