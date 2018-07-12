from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
# local imports
from config import app_config
from flask_bootstrap import Bootstrap


# db variable initialization

db = SQLAlchemy()

login_manager = LoginManager

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    print(10*'*')
    print(config_name)
    print(app_config[config_name])
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    Bootstrap(app)
    db.init_app(app)


    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"

    migrate = Migrate(app, db)

    from app import models

    @app.route('/')
    def hello_world():
        return 'Hello World!'

    return app
