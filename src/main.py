from fastapi import FastAPI
from routes import BaseRoute, UserRecommendationRoute

app = FastAPI()

app.include_router(BaseRoute.base_router)
app.include_router(UserRecommendationRoute.user_recommendation_router)