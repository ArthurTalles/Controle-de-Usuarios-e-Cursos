from flask import request, jsonify
from .models import Course, db

def list_courses():
    courses = Course.query.all()
    return jsonify([course.title for course in courses])

def add_course():
    data = request.get_json()
    new_course = Course(title=data['title'], description=data['description'])
    db.session.add(new_course)
    db.session.commit()
    return jsonify({'message': 'Course added successfully'}), 201

def view_course(course_id):
    course = Course.query.get_or_404(course_id)
    return jsonify({'title': course.title, 'description': course.description})
