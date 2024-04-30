from flask import Blueprint

courses_bp = Blueprint('courses', __name__)

from . import routes
