from src.presenters.controllers.starship_information_colector_controller import StarshipInformationColectorController
from src.data.usescases.starship_information_colector import StarshipInformationColector
from src.infra.swapi_api_consumer import SwapiApiConsumer

def get_starship_information_composer():
    ''' Composer '''

    infra = SwapiApiConsumer()
    usecase = StarshipInformationColector(infra)
    controller = StarshipInformationColectorController(usecase)

    return controller
