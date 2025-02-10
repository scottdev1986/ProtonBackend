from pydantic import BaseModel


class Hello(BaseModel):
    name: str
    age: int
    city: str
