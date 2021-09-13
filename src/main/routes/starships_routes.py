from fastapi import APIRouter, Request as RequestFastApi
from src.validators.get_starships_in_pagination_validator import get_pagination_validator

starships_routes = APIRouter()

@starships_routes.get("/api/starships/list")
def get_starships_in_pagination(request: RequestFastApi):
    ''' get_starships_in_pagination '''

    get_pagination_validator(request)

    return { "Ola": "Mundo" }
