from http import HTTPStatus

from sanic import Blueprint
from sanic.exceptions import NotFound
from sanic.response import json

from core.helpers import jsonapi

blueprint = Blueprint('core.extentions.exceptions')

@blueprint.exception(NotFound)
def handle_404(request, exception):
    '''Handle 404 Not Found

    This handler should be used to handle error http 404 not found for all
    endpoints or if resource not available.
    '''
    error = jsonapi.format_error(title='Resource not found', detail=str(exception))
    return json(jsonapi.return_an_error(error), status=HTTPStatus.NOT_FOUND) 
