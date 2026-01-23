from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    enrollment_year = db.Column(db.Integer, nullable=False)
    department = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    academic_records = db.relationship('AcademicRecord', backref='student', lazy=True)
    skills = db.relationship('Skill', backref='student', lazy=True)
    career_goals = db.relationship('CareerGoal', backref='student', lazy=True)

class AcademicRecord(db.Model):
    __tablename__ = 'academic_records'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    semester = db.Column(db.Integer, nullable=False)
    gpa = db.Column(db.Float, nullable=False)
    courses = db.Column(db.JSON, nullable=True)

class Skill(db.Model):
    __tablename__ = 'skills'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    skill_name = db.Column(db.String(100), nullable=False)
    proficiency_level = db.Column(db.Integer, nullable=False) # 1-10
    verified = db.Column(db.Boolean, default=False)

class CareerGoal(db.Model):
    __tablename__ = 'career_goals'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=False)
    target_role = db.Column(db.String(100), nullable=False)
    target_industry = db.Column(db.String(100), nullable=False)
