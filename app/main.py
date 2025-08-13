from fastapi import FastAPI
from app.api.routes import auth

app = FastAPI(title="Сервис Авторизации")

app.include_router(auth.router, prefix="/auth", tags=["auth"])

@app.get("/")
def root():
    return {"message": "Сервис авторизации работает"}

