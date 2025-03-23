from App import create_app
from App.extensions import socketio  # Import socketio từ extensions.py

app = create_app()

if __name__ == "__main__":
    socketio.run(app, debug=True)  # Sử dụng socketio.run thay vì app.run