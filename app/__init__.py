from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from settings import config_dict

db = SQLAlchemy()


def create_app(config=config_dict["dev"]):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)

    from app.main.views import blueprint as main
    from app.api import blueprint as api

    app.register_blueprint(main)
    app.register_blueprint(api)

    return app
