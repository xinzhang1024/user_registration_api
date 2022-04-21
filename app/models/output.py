
from pydantic import BaseModel


class RegisterOutput(BaseModel):
    status: str
    message: str


class EmailValidationOutput(BaseModel):
    status: str
    email_verified: bool
