from fastapi import FastAPI
from app.routers import hello

# Creates app instance
app = FastAPI()

app.include_router(
    hello.router,
    prefix="/hello",
    tags=["hello"],
)


@app.get("/")
def root():
    return {"status": "ok"}
