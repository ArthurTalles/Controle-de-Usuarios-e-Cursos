from flask import request, jsonify
from .models import User
from ..extensions import db
from flask_jwt_extended import  create_access_token, get_jwt, get_jwt_identity, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash

def register_user():
    data = request.get_json()

    if not data or 'username' not in data or 'password_hash' not in data:
        return jsonify({"message": "username or password not provided"}), 400

    username = data['username']
    password = data['password_hash']

    # Verifique se a senha não é vazia
    if not password.strip():
        return jsonify({"message": "Password is empty"}), 400

    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
    new_user = User(username=username, password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201

def login_user():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and check_password_hash(user.password_hash, data['password_hash']):
        access_token = create_access_token(identity=user.username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"message": "Invalid username or password"}), 401

def protected_user():
    current_user_id = get_jwt_identity()
    return jsonify(logged_in_as=current_user_id), 200

class RevokedToken(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(120), nullable=False)

@jwt_required()
def user_logout():
    jti = get_jwt()['jti']
    try:
        revoked_token = RevokedToken(jti=jti)
        db.session.add(revoked_token)
        db.session.commit()
        return jsonify({"message": "User logged out successfully"}), 200
    except:
        return jsonify({"message": "Logout failed"}), 500
