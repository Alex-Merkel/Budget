from flask import Flask, Blueprint

from .site.routes import site
from .api.routes import api
from .models import db
from config import Config
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(site)
    app.register_blueprint(api)

    app.config.from_object(Config)
    db.init_app(app)

    return app