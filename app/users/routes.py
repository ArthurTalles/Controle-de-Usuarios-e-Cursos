from . import users_bp
from .controllers import register_user, login_user, user_logout

@users_bp.route('/register', methods=['POST'])
def register():
    return register_user()

@users_bp.route('/login', methods=['POST'])
def login():
    return login_user()

@users_bp.route('/logout', methods=['POST'])
def logout():
    return user_logout()
