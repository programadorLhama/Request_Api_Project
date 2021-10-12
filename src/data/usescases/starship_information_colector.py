from typing import Type, Dict
from src.domain.usecases.starship_information_colector import StarshipInformationColectorInterface
from src.data.interfaces.swapi_api_consumer import SwapiApiConsumerInterface
from src.errors import HttpUnprocessableEntityError


class StarshipInformationColector(StarshipInformationColectorInterface):
    ''' StarshipInformationColector usecase '''

    def __init__(self, api_consumer: Type[SwapiApiConsumerInterface]) -> None:
        self.__api_consumer = api_consumer

    def find_starship(self, starship_id: int, time: str) -> Dict:
        '''
            Find starship information and return it
            :param  - starship_id: Id of the starship
                    - time: Time in hours
            :returns - Dictionary with starship information
        '''

        starship_information = self.__search_starship(starship_id)
        mglt = starship_information['MGLT']

        distance_traveld = self.__calculate_distance_traveled_to_spaceship(mglt, time)

        formated_response = self.__format_response(starship_information, distance_traveld)
        return formated_response

    def __search_starship(self, starship_id: int) -> Dict:
        '''
            Get Starship aind validade information
            :param - starship_id: Id of the starship
            :returns - Dictionary with starship information from API
        '''

        api_response = self.__api_consumer.get_starship_information(starship_id)

        if api_response.response['MGLT'] == 'unknown':
            raise HttpUnprocessableEntityError('Unprocessible Information for selected starship')

        return api_response.response

    @classmethod
    def __calculate_distance_traveled_to_spaceship(cls, mglt: str, time: str) -> int:
        '''
            Algorithm to calculate distance traveled
            :param  - mglt: string with Maximum number of Megalights for this spaceship
                    - time: Time in hours
            :returns - distance traveled in megalights
        '''

        distance_traveled = int(mglt) * int(time)
        return distance_traveled

    @classmethod
    def __format_response(cls, starship_information: Dict, distance_traveled: int) -> Dict:
        return {
            "starship": starship_information["name"],
            "model": starship_information["model"],
            "manufacturer": starship_information["manufacturer"],
            "max_atmosphering_speed": starship_information["max_atmosphering_speed"],
            "MGLT": starship_information["MGLT"],
            "distance_traveled": str(distance_traveled) + " ML"
        }
