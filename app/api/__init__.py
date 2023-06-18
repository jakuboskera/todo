from flask import Blueprint
from flask_restx import Api

from app.api.tasks import api as tasks

blueprint = Blueprint("api", __name__)

authorizations = {"apikey": {"type": "apiKey", "in": "header", "name": "X-API-KEY"}}

api = Api(
    blueprint,
    title="TODO",
    version="1.0",
    description="TODO simple API",
    authorizations=authorizations,
    security="apikey",
)

api.add_namespace(tasks)
