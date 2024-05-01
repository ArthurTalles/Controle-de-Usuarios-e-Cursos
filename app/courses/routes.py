from flask import jsonify, request
from . import courses_bp
from .controllers import create_track, create_course, create_lesson, create_comment, create_review, get_course_details

# endpoint de registro de trilha
@courses_bp.route('/tracks', methods=['POST'])
def track_create():
    data = request.get_json()
    return create_track(data)

# endpoint de registro de curso
@courses_bp.route('/courses', methods=['POST'])
def course_create():
    data = request.get_json()
    return create_course(data)

# endpoint de buscar curso
@courses_bp.route('/courses/<int:course_id>', methods=['GET'])
def course_details(course_id):
    return get_course_details(course_id)

# endpoint de registro aula
@courses_bp.route('/courses/<int:course_id>/lessons', methods=['POST'])
def lesson_create(course_id):
    data = request.get_json()
    user_id = data.get('user_id')
    if not user_id:
        return jsonify({'message': 'User ID is required'}), 400
    return create_lesson(course_id, user_id, data)

# endpoint de registro de comentario
@courses_bp.route('/courses/<int:course_id>/comments', methods=['POST'])
def comment_create(course_id):
    data = request.get_json()
    user_id = data.get('user_id')
    if not user_id:
        return jsonify({'message': 'User ID is required'}), 400
    return create_comment(course_id, user_id, data)

# endpoint de registro de reviews
@courses_bp.route('/courses/<int:course_id>/reviews', methods=['POST'])
def review_create(course_id):
    data = request.get_json()
    user_id = data.get('user_id')
    if not user_id:
        return jsonify({'message': 'User ID is required'}), 400
    return create_review(course_id, user_id, data)
