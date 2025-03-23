from flask import jsonify
from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity, get_jwt

def jwt_middleware(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            verify_jwt_in_request()
            return fn(*args, **kwargs)
        except Exception as e:
            return jsonify({"error": "Vui lòng đăng nhập"}), 401
    return wrapper
