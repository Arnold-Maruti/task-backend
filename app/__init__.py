from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.models import User, Task, Category


migrate = Migrate()
db = SQLAlchemy()

# using the application factory pattern to create the Flask application
def create_app():
    # creating the Flask application
    app=Flask(__name__)

    # loading the configuration from the config.py file
    app.config.from_object('config.Config')

    # initializing the extensions
    migrate.init_app(app, db)
    db.init_app(app)

    # Cross Origin Resource Sharing is a security feature that enables requests to come from specific origins.
    CORS(app,origins=["http://localhost:5173"]) 

    @app.route("/")
    def home():
        return {"message": "Hello, Welcome to My API!"}

    return app