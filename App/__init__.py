from flask import Flask
from App.config import Config
from App.extensions import create_extension
from App.router.auth_router import auth_bp  
from App.router.chat_router import chat_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    create_extension(app)

    app.register_blueprint(auth_bp, url_prefix="/")
    app.register_blueprint(chat_bp, url_prefix="/chat")

    return app
