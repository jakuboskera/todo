from flask.helpers import get_debug_flag
from flask_migrate import Migrate

from app import create_app
from app import db
from settings import config_dict
from os import environ


CONFIG = ""
config = environ.get("TODO_CONFIG", "")
if config != "" and config in config_dict:
    CONFIG = config
else:
    CONFIG = "dev" if get_debug_flag() else "prod"

app = create_app(config_dict[CONFIG])
migrate = Migrate(app, db)
