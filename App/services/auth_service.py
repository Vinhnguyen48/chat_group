import re
import time
from flask_jwt_extended import create_access_token
from App.models.user import User, db
from werkzeug.security import generate_password_hash,check_password_hash
from sqlalchemy import or_

EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

def create_user(username, email, password):
    if not username or not email or not password:
        return "error", "Vui lòng điền đầy đủ thông tin.", 400
    
    if not re.match(EMAIL_REGEX, email):
        return "error", "Email không hợp lệ.", 400
    
    if User.query.filter(or_(User.email == email, User.username == username)).first():
        return "error", "Email hoặc Username đã tồn tại.", 400
    mh_pass = generate_password_hash(password)
    new_user = User(username=username, email=email, password=mh_pass)
    db.session.add(new_user)
    db.session.commit()
    return "success", "Đăng ký thành công.", 200


def login_user(username, password):
    user = User.query.filter_by(username=username).first()

    if not user:
        return "error", "Sai tài khoản hoặc mật khẩu.", 400
    if not check_password_hash(user.password, password):
        return "error", "Sai tài khoản hoặc mật khẩu.", 400
    access_token = create_access_token(identity={"id": user.id, "role": user.role})
    return "success", access_token, 200
    