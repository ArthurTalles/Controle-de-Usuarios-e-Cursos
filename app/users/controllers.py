from flask import request, jsonify
from .models import User
from ..extensions import db
from flask_jwt_extended import  create_access_token, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

def register_user():
    data = request.get_json()

    # Log para verificar os dados recebidos
    print("Data received:", data)

    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"message": "username or password not provided"}), 400

    username = data['username']
    password = data['password']

    # Verifique se a senha não é vazia
    if not password.strip():
        return jsonify({"message": "Password is empty"}), 400

    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201

def login_user():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and check_password_hash(user.password_hash, data['password']):
        access_token = create_access_token(identity=user.username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"message": "Invalid username or password"}), 401


def user_logout():
    jti = get_jwt_identity()['jti']  # JTI é o "JWT ID", um identificador único para um JWT
    try:
        revoked_token = revoked_token(jti=jti)
        db.session.add(revoked_token)
        db.session.commit()
        return jsonify({"message": "User logged out successfully"}), 200
    except:
        return jsonify({"message": "Logout failed"}), 500
