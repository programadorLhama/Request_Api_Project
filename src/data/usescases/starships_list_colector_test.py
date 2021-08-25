from src.infra.test.swapi_api_consumer import SwapiApiConsumerSpy
from .starships_list_colector import StarshipsListColector

def test_list():
    ''' testing list method '''

    api_consumer = SwapiApiConsumerSpy()
    starships_list_colector = StarshipsListColector(api_consumer)

    page = 1
    response = starships_list_colector.list(page)

    assert api_consumer.get_starships_attributes == { "page": page }
    assert isinstance(response, list)
    assert "id" in response[0]
    assert "MGLT" in response[0]
