
from fastapi import FastAPI

from apis.email_validation import EMAIL_VALIDATION_ROUTER
from apis.register import REGISTER_ROUTER

app = FastAPI()
app.include_router(REGISTER_ROUTER)
app.include_router(EMAIL_VALIDATION_ROUTER)


@app.get("/")
async def root():
    return {"message": "Hello World"}

