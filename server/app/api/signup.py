# Vue-Squad/server/app/api/signup.py

from flask_restful import Resource
from flask import request
from ..models import User
from .. import db
from ..custom import is_valid_email, is_valid_username

class SignupApi(Resource):
    def post(self):
        try:
            data = request.get_json()
            email = data.get('email')
            username = data.get('username')

            if email is None:
                return {'message': 'Email address is required!'}, 400
            
            email = email.lower()
            if not is_valid_email(email):
                return {'message': 'Email address is invalid!'}, 400

            email_checker = bool(User.query.filter_by(email=email).first())
            if email_checker:
                return {'message': 'Email address is already in use!'}, 400
            
            if username is None:
                return {'message': 'Username is required!'}, 400
            
            username = username.lower()
            if not is_valid_username(username):
                return {'message': 'Username is invalid!'}, 400
            
            username_checker = bool(User.query.filter_by(username=username).first())
            if username_checker:
                return {'message': 'Username already taken!'}, 400
            
            role = data.get('role')
            if role not in ['Instructor', 'Student']:
                return {'message': 'Invalid role!'}, 400
            
            password = data.get('password')
            confirm_password = data.get('confirm_password')
            if password is None:
                return {'message': 'Password is required!'}, 400
            
            if confirm_password is None:
                return {'message': 'Confirm Password is required!'}, 400
            
            if len(password) < 8:
                return {'message': 'Password must be at least 8 characters!'}, 400
            
            if password != confirm_password:
                return {'message': 'Password and Confirm Password must match!'}, 400
            
        
            # Create a new user
            new_user = User(email=email, username=username, role=role)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.flush()

            # Handle role-specific data creation
            response = new_user.additional_commit(data)
            if response:
                db.session.rollback()
                return response

            db.session.commit()
            return {'message': 'Signup successful!'}, 200

        except Exception as e:
            db.session.rollback()
            return {'message': f'An error occurred: {str(e)}'}, 500
