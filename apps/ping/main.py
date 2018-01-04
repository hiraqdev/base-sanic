from sanic.response import text
from sanic import Blueprint

blueprint = Blueprint('ping_app')

@blueprint.route('/me')
async def ping_me(request):
    return text('pong')
