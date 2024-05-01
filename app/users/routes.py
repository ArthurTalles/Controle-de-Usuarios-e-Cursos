from flask_jwt_extended import jwt_required
from . import users_bp
from .controllers import register_user, login_user, user_logout, protected_user

# endpoint de registro usuário
@users_bp.route('/register', methods=['POST'])
def register():
    return register_user()

# endpoint de login usuário
@users_bp.route('/login', methods=['POST'])
def login():
    return login_user()

# endpoint de logout usuário
@users_bp.route('/logout', methods=['POST'])
def logout():
    return user_logout()

# endpoint de validação token
@users_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return protected_user()
