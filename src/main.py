from fastapi import FastAPI
from routes import BaseRoute, DataRoute

app = FastAPI()

app.include_router(BaseRoute.base_router)
app.include_router(DataRoute.data_router)