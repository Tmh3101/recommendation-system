from fastapi import FastAPI
from pydantic import BaseModel
import dill
import json


app = FastAPI()

recommendation_model = dill.load(open('movies_recommender.sav', 'rb'))

class RecommendRequest(BaseModel):
    movie_name: str


@app.post('/recommend')
def recommend_movies(request: RecommendRequest):
    recommended_movies = recommendation_model.recommend(request.movie_name)
    return { 'recommended_movies': recommended_movies }