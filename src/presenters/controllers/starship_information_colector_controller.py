from typing import Type, Dict
from src.presenters.interface.controllers import ControllersInterface
from src.domain.usecases.starship_information_colector import StarshipInformationColectorInterface

class StarshipInformationColectorController(ControllersInterface):
    ''' Controller to StarshipInformationColector '''

    def __init__(self, starship_information_colector: Type[StarshipInformationColectorInterface]) -> None:
        self.__use_case = starship_information_colector

    def handler(self, http_request: Dict):
        ''' Handler to information colector controller '''

        starship_id = http_request["body"]["starship_id"]
        time = http_request["body"]["time"]

        starship_information = self.__use_case.find_starship(starship_id, time)
        http_response = { "status_code": 200, "data": { "data": starship_information } }

        return http_response
