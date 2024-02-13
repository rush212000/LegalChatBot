from flask import Flask
from models.logger import logger  # Import the custom logger you've set up
from .config import Config

def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Import and register blueprints
    # from .views import main_blueprint
    # app.register_blueprint(main_blueprint)

    @app.route('/')
    def index():
        return "Welcome to LegalContractBot!"

    logger.info("Application initialized")
    return app
