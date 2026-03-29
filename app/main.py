
from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="A/B Testing API")

app.include_router(router)
