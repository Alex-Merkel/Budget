from flask import Flask, Blueprint

from .site.routes import site
from .api.routes import api
from app.models import db
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(site)
    app.register_blueprint(api)

    return app