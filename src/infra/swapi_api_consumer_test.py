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

def test_get_starship_information(requests_mock):
    ''' Testing get_starship_information method '''

    starship_id = 9
    swapi_api_consumer = SwapiApiConsumer()

    requests_mock.get(
        'https://swapi.dev/api/starships/{}/'.format(starship_id),
        status_code=200,
        json={'name': 'some', 'model': 'thing', 'MGLT': '123'}
    )

    starship_information = swapi_api_consumer.get_starship_information(starship_id)

    assert starship_information.request.method == 'GET'
    assert starship_information.request.url == 'https://swapi.dev/api/starships/{}/'.format(starship_id)
    assert starship_information.status_code == 200

    assert "MGLT" in starship_information.response


def test_get_starship_information_eror(requests_mock):
    ''' Testing get_starship_information method in error '''

    starship_id = 1
    swapi_api_consumer = SwapiApiConsumer()

    requests_mock.get(
        'https://swapi.dev/api/starships/{}/'.format(starship_id),
        status_code=404,
        json={'detail': 'something'}
    )

    try:
        swapi_api_consumer.get_starship_information(starship_id)
        assert True is False
    except HttpRequestError as error:
        assert error.message is not None
        assert error.status_code is not None
