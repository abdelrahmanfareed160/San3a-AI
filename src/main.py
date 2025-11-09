from fastapi import FastAPI
from routes import BaseRouter, DataRoute

app = FastAPI()

app.include_router(BaseRouter.base_router)
app.include_router(DataRoute.data_router)