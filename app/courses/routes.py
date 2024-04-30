from . import courses_bp
from .controllers import list_courses, add_course, view_course

@courses_bp.route('/')
def index():
    return list_courses()

@courses_bp.route('/add', methods=['POST'])
def add():
    return add_course()

@courses_bp.route('/<int:course_id>')
def show(course_id):
    return view_course(course_id)
