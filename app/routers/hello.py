from fastapi import APIRouter, status, Response
from app.models.hello import Hello


router = APIRouter()


@router.get("/")
async def hello(response: Response):
    m = Hello(name="John", age=25, city="New York")
    return {"user": m}
