# Vue-Squad/server/app/models/user.py

from .. import db
from ..custom import IndianZone
from werkzeug.security import generate_password_hash, check_password_hash
from .instructor import Instructor
from .student import Student

class User(db.Model):
    __tablename__ = 'users'
    
    # Columns
    user_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255))
    role = db.Column(db.String(25), nullable=False)
    created_at = db.Column(db.DateTime, default=IndianZone())
    
    # Relationships
    instructor = db.relationship('Instructor', back_populates='user', uselist=False, cascade='all, delete-orphan')
    student = db.relationship('Student', back_populates='user', uselist=False, cascade='all, delete-orphan')
    
    # Methods
    def set_password(self, password=None):
        if password:
            self.password = generate_password_hash(password)
    
    def check_password(self, password):
        if self.password:
            return check_password_hash(self.password, password)
        return False
    
    def additional_commit(self, data):
        name = data.get('name')
        if self.role == 'Instructor':
            new_instructor = Instructor(user_id=self.user_id, name=name)
            db.session.add(new_instructor)
        elif self.role == 'Student':
            if not name:
                return {'message': "Student's Name is missing!"}, 400
            new_student = Student(user_id=self.user_id, name=name)
            db.session.add(new_student)
        else:
            return {'message': "Invalid role specified!"}, 400
