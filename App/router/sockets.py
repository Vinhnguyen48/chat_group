from flask_socketio import emit
from extensions import db, socketio
from models.message import GroupMessage
from models.user import User

@socketio.on("send_message")
def handle_message(data):
    sender_id = data.get("sender_id")
    content = data.get("content")

    user = User.query.get(sender_id)
    if not user:
        return

    message = GroupMessage(sender_id=sender_id, content=content)
    db.session.add(message)
    db.session.commit()

    emit("receive_message", {
        "sender": user.username,
        "content": content,
        "timestamp": message.timestamp.strftime("%Y-%m-%d %H:%M:%S")
    }, broadcast=True)
