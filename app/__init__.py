from flask import Flask
from app.routes.Planets_routes import Planets_bp

def create_app(test_config=None):
    app = Flask(__name__)
    app.register_blueprint(Planets_bp)
    return app
