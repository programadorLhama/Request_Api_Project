from fastapi import APIRouter, Request as RequestFastApi
from fastapi.responses import JSONResponse

from src.validators.get_starships_in_pagination_validator import get_pagination_validator
from src.validators.get_starship_information_validator import get_starship_information_validator

from src.main.adapters import request_adapter
from src.main.composer.get_starships_in_pagination_composer import get_starships_in_pagination_composer
from src.main.composer.get_starship_information_composer import get_starship_information_composer

from src.presenters.errors.error_controller import handle_errors

starships_routes = APIRouter()

@starships_routes.get("/api/starships/list")
async def get_starships_in_pagination(request: RequestFastApi):
    ''' get_starships_in_pagination '''

    response = None
    controller = get_starships_in_pagination_composer()

    try:
        get_pagination_validator(request)
        response = await request_adapter(request, controller.handler)
    except Exception as e:
        response = handle_errors(e)

    return JSONResponse(
        status_code=response["status_code"],
        content=response["data"]
    )

# Essa rota fica melhor com get!
@starships_routes.post("/api/starships/information")
async def get_starship_information(request: RequestFastApi):
    ''' get_starship_information '''

    response = None
    controller = get_starship_information_composer()

    try:
        await get_starship_information_validator(request)
        response = await request_adapter(request, controller.handler)
    except Exception as e:
        response = handle_errors(e)

    return JSONResponse(
        status_code=response["status_code"],
        content=response["data"]
    )
