from http import HTTPStatus

from sanic import Blueprint
from sanic.response import json

from core.helpers import jsonapi

blueprint = Blueprint('core.extentions.middlewares')
DEFAULT_TYPE = 'application/vnd.api+json'

@blueprint.middleware('response')
def jsonapi_standard_response_header(request, response):
    '''Adding custom content type to all responses

    Following JSON API standard, all response headers should
    has a content-type with value is application/vnd.api+json
    '''
    response.headers['Content-Type'] = DEFAULT_TYPE 

@blueprint.middleware('request')
def check_content_negotiation(request):
    '''Checking current request header content negotiation

    All request should accept application/vnd.api+json or it will
    not allowed to continue process, and throw a http status code's 406

    For all requests that not using GET http method, should has 
    a content-type header parameter with value is application/vnd.api+json
    if not will throw a http status code's 415
    '''
    accept = request.headers.get('accept')
    content_type = request.headers.get('content-type', None)
    method = request.method

    if accept != DEFAULT_TYPE:
        error = jsonapi.format_error(title='Not Acceptable', detail='Cannot continue process for your requested media type.')
        return json(jsonapi.return_an_error(error), status=HTTPStatus.NOT_ACCEPTABLE)

    if method != 'GET':
        if content_type != DEFAULT_TYPE:
            error = jsonapi.format_error(title='Unsupported Media Type', detail='Cannot continue process for your requested media type.')
            return json(jsonapi.return_an_error(error), status=HTTPStatus.UNSUPPORTED_MEDIA_TYPE)
