from fastapi import APIRouter, status, Response, Security
from app.models.hello import Hello
from app.utils.auth import VerifyToken

router = APIRouter()
auth = VerifyToken()


@router.get("/")
async def hello(response: Response, auth_result: str = Security(auth.verify)):
    m = Hello(name="John", age=25, city="New York")
    return {"user": m, "auth_result": auth_result}
