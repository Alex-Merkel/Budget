from flask import Flask
from config import Config
from .site.routes import site
from .authentication.routes import auth
from .api.routes import api

from flask_migrate import Migrate
from models import db, login_manager, ma
from flask_cors import CORS
from helpers import JSONEncoder


def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(site)
    app.register_blueprint(auth)
    app.register_blueprint(api)

    app.json_encoder = JSONEncoder
    app.config.from_object(Config)
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.signin"
    ma.init_app(app)
    migrate = Migrate(app, db)

    return app