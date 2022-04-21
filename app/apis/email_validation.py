
from fastapi import APIRouter, Depends
from pydantic import constr

from config import REGISTER_TAG
from models.output import EmailValidationOutput
from utils.check_auth import check_user_and_code

EMAIL_VALIDATION_ROUTER = APIRouter()


@EMAIL_VALIDATION_ROUTER.get('/email_validation/{code}', tags=[REGISTER_TAG], response_model=EmailValidationOutput)
def email_validation(code: constr(regex='^\d{4}$'), db_code: str = Depends(check_user_and_code)):
    return {
        'status': 'OK' if code == db_code else 'KO',
        'email_verified': True if code == db_code else False
    }
