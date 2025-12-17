from fastapi import FastAPI
from app.health import router

app = FastAPI()
app.include_router(router)
