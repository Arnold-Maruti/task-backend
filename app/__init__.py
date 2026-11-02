from flask import Flask
from flask_cors import CORS

# using the application factory pattern to create the Flask application
def create_app():
    # creating the Flask application
    app=Flask(__name__)

    # Cross Origin Resource Sharing is a security feature that enables requests to come from specific origins.
    CORS(app,origins=["http://localhost:5173"]) 

    @app.route("/")
    def home():
        return {"message": "Hello, Welcome to My API!"}

    return app