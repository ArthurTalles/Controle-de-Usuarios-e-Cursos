from flask import jsonify, request
from . import courses_bp
from .controllers import create_track, create_course, create_lesson, create_comment, create_review

@courses_bp.route('/tracks', methods=['POST'])
def track_create():
    data = request.get_json()
    return create_track(data)

@courses_bp.route('/courses', methods=['POST'])
def course_create():
    data = request.get_json()
    return create_course(data)

@courses_bp.route('/courses/<int:course_id>/lessons', methods=['POST'])
def lesson_create(course_id):
    data = request.get_json()
    user_id = data.get('user_id')
    if not user_id:
        return jsonify({'message': 'User ID is required'}), 400
    return create_lesson(course_id, user_id, data)

@courses_bp.route('/courses/<int:course_id>/comments', methods=['POST'])
def comment_create(course_id):
    data = request.get_json()
    user_id = data.get('user_id')
    if not user_id:
        return jsonify({'message': 'User ID is required'}), 400
    return create_comment(course_id, user_id, data)

@courses_bp.route('/courses/<int:course_id>/reviews', methods=['POST'])
def review_create(course_id):
    data = request.get_json()
    user_id = data.get('user_id')
    if not user_id:
        return jsonify({'message': 'User ID is required'}), 400
    return create_review(course_id, user_id, data)
