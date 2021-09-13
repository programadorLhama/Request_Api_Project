from typing import Dict
from src.domain.usecases.starships_list_colector import StarshipsListColectorInterface
from src.presenters.interface.controllers import ControllersInterface

class StarshipsListColectorController(ControllersInterface):
    ''' Controller to List Starships '''

    def __init__(self, starships_list_colector: StarshipsListColectorInterface) -> None:
        self.__use_case = starships_list_colector

    def handler(self, http_request: Dict):
        ''' Handler to list colector '''

        page = http_request["query_params"]["page"]

        starships_list = self.__use_case.list(page)
        http_response = { "status_code": 200, "data": { "data": starships_list } }

        return http_response
