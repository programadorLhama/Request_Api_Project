from typing import Callable
from fastapi import Request as RequestFastApi

async def request_adapter(request: RequestFastApi, callback: Callable):
    '''
        Adapter to httpRequest
        @param - request: Http request Object with all properties
                 callback: Calback to process http request
        @return - Http Response to Request
    '''

    body = None

    try:
        body = await request.json()
    except:
        pass

    http_request = {
        "query_params": request.query_params,
        "body": body
    }

    http_response = callback(http_request)
    return http_response
