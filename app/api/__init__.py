from flask import Flask
from app.api.product.routes import product_blueprint
from app.api.base_model import db
from app.config import config

def create_app(config_name):
    """
        Create flask instance using application factory pattern
        args :
            config_name -- Configuration key used (DEV/PROD/TESTING)
    """
    app = Flask(__name__)

    app.config.from_object(config.CONFIG_BY_NAME[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    return app                  