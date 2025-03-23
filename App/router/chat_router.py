from flask import Blueprint, request, jsonify,render_template
from App.models.message import GroupMessage
from flask_jwt_extended import get_jwt_identity
from App.extensions import db
from App.Middleware.jwt_middlewares import jwt_middleware
chat_bp = Blueprint("chat", __name__, url_prefix="/chat")

@chat_bp.route("/")
@jwt_middleware
def chat_index():
    return render_template("pages/chat.html")
@chat_bp.route("/messages", methods=["GET"])
@jwt_middleware
def get_messages():
    messages = GroupMessage.query.order_by(GroupMessage.timestamp.asc()).all()
    return jsonify([{"sender": msg.sender_id, "content": msg.content, "timestamp": msg.timestamp} for msg in messages])

@chat_bp.route("/messages", methods=["POST"])
@jwt_middleware
def send_message():
    data = request.json
    sender_id = get_jwt_identity()

    msg = GroupMessage(sender_id=sender_id, content=data["content"])
    db.session.add(msg)
    db.session.commit()

    return jsonify({"message": "Message sent!"}), 201
