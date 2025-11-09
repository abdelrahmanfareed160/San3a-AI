from fastapi import FastAPI
from routes import BaseRouter

app = FastAPI()

app.include_router(BaseRouter.base_router)