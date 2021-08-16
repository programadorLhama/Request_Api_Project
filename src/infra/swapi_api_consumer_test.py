from src.errors import HttpRequestError
from .swapi_api_consumer import SwapiApiConsumer


def test_get_starships(requests_mock):
    ''' Testing get_starships method '''

    requests_mock.get('https://swapi.dev/api/starships/', status_code=200, json={ 'some': 'thing', "results": [{}] })

    swapi_api_consumer = SwapiApiConsumer()
    page = 1

    get_starships_response = swapi_api_consumer.get_starships(page=page)

    assert get_starships_response.request.method == 'GET'
    assert get_starships_response.request.url == 'https://swapi.dev/api/starships/'
    assert get_starships_response.request.params == { "page": page }

    assert get_starships_response.status_code == 200
    assert isinstance(get_starships_response.response["results"], list)

def test_get_starships_http_error(requests_mock):
    ''' Testing error in get_starships method '''

    requests_mock.get('https://swapi.dev/api/starships/', status_code=404, json={ 'detail': 'something' })

    swapi_api_consumer = SwapiApiConsumer()
    page = 100

    try:
        swapi_api_consumer.get_starships(page=page)
        assert True is False
    except HttpRequestError as error:
        assert error.message is not None
        assert error.status_code is not None
