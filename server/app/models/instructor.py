# Vue-Squad/server/app/models/instructor.py

from .. import db
from ..custom import IndianZone

class Instructor(db.Model):
    __tablename__ = 'instructors'
    
    # Columns
    instructor_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    bio = db.Column(db.String(255))
    experience = db.Column(db.Numeric(3,1))
    
    # Relationships
    user = db.relationship('User', back_populates='instructor', uselist=False)
    # courses = db.relationship('Course', back_populates='instructor', cascade='all, delete-orphan')