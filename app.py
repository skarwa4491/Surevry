from flask import Flask
import os
from db import db
from flask_smorest import Api
from resources.survey import blp as survey_blue_print
from resources.question import blp as question_blue_print
from resources.options import blp as option_blue_print
import models
def create_app(db_url=None):
    app = Flask(__name__)
    app.config["PROPOGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Store REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    db.init_app(app)
    with app.app_context(): # this is updated , instead of @app.before_first_request
        db.create_all()
    api = Api(app)
    api.register_blueprint(survey_blue_print)
    api.register_blueprint(question_blue_print)
    api.register_blueprint(option_blue_print)
    return app