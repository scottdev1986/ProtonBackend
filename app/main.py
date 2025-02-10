from fastapi import FastAPI

# Creates app instance
app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "ok"}