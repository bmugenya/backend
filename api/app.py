
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import configurations
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
migrate = Migrate()
cors = CORS()

def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app,db)
    cors.init_app(app)
    

def register_blueprints(app):
    from api.users import users
    app.register_blueprint(users)


def create_app(configuration):
    app = Flask(__name__)
    app.config.from_object(configurations[configuration])

    from api import models
    register_extensions(app)
    register_blueprints(app)
 

    return app
