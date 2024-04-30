# controllers.py
from flask import jsonify, request
from .models import db, Track, Course, Lesson, Comment, Review

def create_track(data):
    new_track = Track(name=data['name'], description=data.get('description', ''))
    db.session.add(new_track)
    db.session.commit()
    return jsonify({'message': 'Track created successfully', 'track_id': new_track.id}), 201

def create_course(data):
    new_course = Course(title=data['title'], description=data.get('description', ''))
    db.session.add(new_course)
    db.session.commit()
    return jsonify({'message': 'Course created successfully', 'course_id': new_course.id}), 201

def create_lesson(course_id, user_id, data):
    new_lesson = Lesson(title=data['title'], course_id=course_id, user_id=user_id)
    db.session.add(new_lesson)
    db.session.commit()
    return jsonify({'message': 'Lesson added successfully', 'lesson_id': new_lesson.id}), 201

def create_comment(course_id, user_id, data):
    new_comment = Comment(content=data['content'], course_id=course_id, user_id=user_id)
    db.session.add(new_comment)
    db.session.commit()
    return jsonify({'message': 'Comment added successfully', 'comment_id': new_comment.id}), 201

def create_review(course_id, user_id, data):
    new_review = Review(rating=data['rating'], feedback=data.get('feedback', ''), course_id=course_id, user_id=user_id)
    db.session.add(new_review)
    db.session.commit()
    return jsonify({'message': 'Review added successfully', 'review_id': new_review.id}), 201