from flask import Flask,jsonify
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


sqlalchemy = SQLAlchemy()
migrate = Migrate()
def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object(Config)

    initialize_extensions(app)
    register_blueprints(app)
    
    # Create database tables if they do not exist
    # within flask application context
    with app.app_context():
        sqlalchemy.create_all()

    return app

def initialize_extensions(app):
    # Initialize flask-extensions
    sqlalchemy.init_app(app)
    migrate.init_app(app, sqlalchemy)

def register_blueprints(app):
    from app.api import api

    # Register Blueprints
    app.register_blueprint(api)