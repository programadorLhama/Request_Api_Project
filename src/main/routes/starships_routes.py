from fastapi import APIRouter, Request as RequestFastApi
from fastapi.responses import JSONResponse
from src.validators.get_starships_in_pagination_validator import get_pagination_validator
from src.main.adapters import request_adapter
from src.main.composer.get_starships_in_pagination_composer import get_starships_in_pagination_composer

starships_routes = APIRouter()

@starships_routes.get("/api/starships/list")
async def get_starships_in_pagination(request: RequestFastApi):
    ''' get_starships_in_pagination '''

    get_pagination_validator(request)
    controller = get_starships_in_pagination_composer()

    response = await request_adapter(request, controller.handler)

    return JSONResponse(
        status_code=response["status_code"],
        content=response["data"]
    )
