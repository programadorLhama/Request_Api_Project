from src.presenters.controllers.starships_list_colector_controller import StarshipsListColectorController
from src.data.usescases.starships_list_colector import StarshipsListColector
from src.infra.swapi_api_consumer import SwapiApiConsumer

def get_starships_in_pagination_composer():
    ''' Composer '''

    infra = SwapiApiConsumer()
    usecase = StarshipsListColector(infra)
    controller = StarshipsListColectorController(usecase)

    return controller
