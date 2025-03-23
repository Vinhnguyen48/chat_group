from flask_sqlalchemy import SQLAlchemy 
from flask_jwt_extended import JWTManager
from flask_socketio import SocketIO

db = SQLAlchemy()
jwt=JWTManager()
socketio = SocketIO(cors_allowed_origins="*")


def create_extension(app):
    db.init_app(app)
    jwt.init_app(app)
    socketio.init_app(app)