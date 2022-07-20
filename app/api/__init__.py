from flask import Blueprint
from flask_restx import Api

from app.api.tasks import api as tasks

blueprint = Blueprint("api", __name__, url_prefix="/api/v1")

api = Api(blueprint, title="TODO", version="1.0", description="TODO simple API")

api.add_namespace(tasks)
