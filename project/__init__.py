# project/__init__.py


import os

from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt


# instantiate the extensions
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()


def create_app():

    # instantiate the app
    app = Flask(__name__)

    # enable CORS
    CORS(app)

    # set config
    app_settings = "project.config.TestingConfig"
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    # register blueprints
    from project.api.resources.users import users_blueprint
    from project.api.resources.auth import auth_blueprint
    from project.api.resources.quotes import quotes_blueprint
    from project.api.resources.jobs import jobs_blueprint
    from project.api.resources.friends import friends_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(users_blueprint)
    app.register_blueprint(quotes_blueprint)
    app.register_blueprint(jobs_blueprint)
    app.register_blueprint(friends_blueprint)

    return app
