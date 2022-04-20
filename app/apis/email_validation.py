
from fastapi import APIRouter
from pydantic import constr

from config import REGISTER_TAG
from services.db_service import read_from_db

EMAIL_VALIDATION_ROUTER = APIRouter()


@EMAIL_VALIDATION_ROUTER.get('/email_validation/{code}', tags=[REGISTER_TAG])
def email_validation(code: constr(regex='^\d{4}$')):

    res = read_from_db(code)
    status = 'OK' if res else 'KO'

    return {
        'status': status,
        'email_verified': res
    }
