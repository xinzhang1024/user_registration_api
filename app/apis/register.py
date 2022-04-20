
from fastapi import APIRouter, Form

from config import REGISTER_TAG
from services.register import register_service

REGISTER_ROUTER = APIRouter()


@REGISTER_ROUTER.post('/register', tags=[REGISTER_TAG])
def register(email: str = Form(..., regex='^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$'), password: str = Form(...)):
    return register_service(email, password)
