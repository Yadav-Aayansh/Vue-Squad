# Vue-Squad/server/app/models/student.py

from .. import db
from ..custom import IndianZone

class Student(db.Model):
    __tablename__ = 'students'
    
    # Columns
    student_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    profile_picture = db.Column(db.String(50), default='student.svg')
    
    # Relationships
    user = db.relationship('User', back_populates='student', uselist=False)
