from typing import Type, Dict
from src.errors import HttpRequestError, HttpUnprocessableEntityError

def handle_errors(error: Type[Exception]) -> Dict:
    '''
        Handler to treat Exception cases
        @param: error - Exception
        @returns: Dict with data and status_code
    '''
    if isinstance(error, HttpRequestError):
        return {
            "data": { "error": error.message },
            "status_code": error.status_code
        }
    elif isinstance(error, HttpUnprocessableEntityError):
        return {
            "data": { "error": error.message },
            "status_code": error.status_code
        }
    else:
        return {
            "data": { "error": str(error) },
            "status_code": 500
        }
