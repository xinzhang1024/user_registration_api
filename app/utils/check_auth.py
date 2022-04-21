
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.status import HTTP_401_UNAUTHORIZED

from services.db_service import read_from_db

security = HTTPBasic()


def check_user_and_code(credentials: HTTPBasicCredentials = Depends(security)):
    code = read_from_db(credentials.username, credentials.password)

    if not code:
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return code
