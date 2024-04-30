from flask import Flask
from config import DevelopmentConfig
from .extensions import db, migrate
from .users import users_bp
from .courses import courses_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)

    app.config.from_object(DevelopmentConfig)
    app.register_blueprint(users_bp, url_prefix='/users')
    app.register_blueprint(courses_bp, url_prefix='/courses')

    return app