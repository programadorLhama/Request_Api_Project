from cerberus import Validator
from src.errors import HttpUnprocessableEntityError

async def get_starship_information_validator(request: any):
    ''' starship information validator '''

    body = None

    try:
        body = await request.json()
    except:
        pass

    body_validator = Validator({
        'starship_id': {'type': 'integer', 'required': True},
        'time': {'type': 'integer', 'required': True}
    })

    response = body_validator.validate(body)

    if response is False:
        raise HttpUnprocessableEntityError(body_validator.errors)
