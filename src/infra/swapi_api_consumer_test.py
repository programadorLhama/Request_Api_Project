from .swapi_api_consumer import SwapiApiConsumer

def test_get_starships():
    ''' Testing get_starships method '''

    swapi_api_consumer = SwapiApiConsumer()
    response = swapi_api_consumer.get_starships(page=1)

    print(response)
