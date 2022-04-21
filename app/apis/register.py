
from fastapi import APIRouter, Form

from config import REGISTER_TAG
from models.output import RegisterOutput
from services.register import register_service

REGISTER_ROUTER = APIRouter()


@REGISTER_ROUTER.post('/register', tags=[REGISTER_TAG], response_model=RegisterOutput)
def register(email: str = Form(..., regex='^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$'), password: str = Form(...)):
    if register_service(email, password):
        return {
            'status': 'OK',
            'message': f'4 digits code has been sent to your email {email}, please input in one minute.'
        }
    else:
        return {
            'status': 'KO',
            'message': 'failed'
        }
