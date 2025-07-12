from fastapi import FastAPI
from backend.src.routers import auth, profile

app = FastAPI()

app.include_router(auth.router)
app.include_router(profile.router)

@app.get("/health")
def health_check():
    return {"status": "ok"} 