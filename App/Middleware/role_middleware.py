from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt


def role_required(role):
    def wrapper(fn):
        @wraps(fn)
        def inner_wrapper(*args, **kwargs):
            claims = get_jwt()
            if claims.get("role") != role:
                return jsonify({"message": "bạn không có quyền truy câp"}), 403
            return fn(*args, **kwargs)
        return inner_wrapper
    return wrapper
