from flask import jsonify, request
from .models import db, Track, Course, Lesson, Comment, Review

def create_track(data):
    if 'name' not in data or not data['name']:
        return jsonify({'error': 'Name is required'}), 400
    new_track = Track(name=data['name'], description=data.get('description', ''))
    db.session.add(new_track)
    db.session.commit()
    return jsonify({'message': 'Track created successfully', 'track_id': new_track.id}), 201

def get_course_details(course_id):

    course = Course.query.filter_by(id=course_id).first()
    if not course:
        return jsonify({'error': 'Course not found'}), 404

    course_data = {
        'id': course.id,
        'title': course.title,
        'description': course.description,
        'lessons': [{'id': lesson.id, 'title': lesson.title} for lesson in course.lessons],
        'comments': [{'id': comment.id, 'content': comment.content, 'user_id': comment.user_id} for comment in course.comments]
    }
    return jsonify(course_data), 200

def create_course(data):
    if 'title' not in data or not data['title']:
        return jsonify({'error': 'Title is required'}), 400  
    new_course = Course(title=data['title'], description=data.get('description', ''))
    db.session.add(new_course)
    db.session.commit()
    return jsonify({'message': 'Course created successfully', 'course_id': new_course.id}), 201

def create_lesson(course_id, user_id, data):
    if 'title' not in data or not data['title']:
        return jsonify({'error': 'Title is required'}), 400    
    new_lesson = Lesson(title=data['title'], course_id=course_id, user_id=user_id)
    db.session.add(new_lesson)
    db.session.commit()
    return jsonify({'message': 'Lesson added successfully', 'lesson_id': new_lesson.id}), 201

def create_comment(course_id, user_id, data):
    if 'content' not in data or not data['content']:
        return jsonify({'error': 'Content is required'}), 400   
    new_comment = Comment(content=data['content'], course_id=course_id, user_id=user_id)
    db.session.add(new_comment)
    db.session.commit()
    return jsonify({'message': 'Comment added successfully', 'comment_id': new_comment.id}), 201

def create_review(course_id, user_id, data):
    if 'rating' not in data or not isinstance(data['rating'], int):
        return jsonify({'error': 'Rating is required and must be an integer'}), 400
    new_review = Review(rating=data['rating'], feedback=data.get('feedback', ''), course_id=course_id, user_id=user_id)
    db.session.add(new_review)
    db.session.commit()
    return jsonify({'message': 'Review added successfully', 'review_id': new_review.id}), 201