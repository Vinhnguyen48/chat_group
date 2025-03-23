from flask import Blueprint, redirect, render_template, request, jsonify, session, url_for
from App.services.auth_service import create_user, login_user
from App.router.chat_router import chat_bp
auth_bp = Blueprint('auth', __name__,)

@auth_bp.route("/")  
def index_register():
    return render_template("pages/Register.html")

@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        data = request.json 
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        if not username or not password or not email:
            return jsonify({"error": "Vui lòng điền đầy đủ thông tin"}), 400
        status, message, status_code = create_user(username, email, password)
        return jsonify({"status": status, "message": message}), status_code

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@auth_bp.route('/home', methods=['GET'])
def home():
    return render_template("pages/home.html")
@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return jsonify({"error": "Vui lòng điền đầy đủ thông tin"}), 400

        status, access_token= login_user(username, password)

        if status == "success":
            session['access_token'] = access_token
            return redirect(url_for('chat.chat_index'))  
    except Exception as e:
        return jsonify({"error": str(e)}), 500