# HomeMate/server/app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS

db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate()

def app_creator(MyConfig):
    app = Flask(__name__)
    app.config.from_object(MyConfig)
    db.init_app(app)
    api = Api(app)
    jwt.init_app(app)

    CORS(app, resources={r"/*": {"origins": app.config.get('FRONTEND_URL'), "supports_credentials": True}})

    from .models import User, Instructor, Student
    with app.app_context():
        db.create_all()

    from .api import SignupApi, TokenApi
    
    api.add_resource(SignupApi, '/api/signup')
    # api.add_resource(LoginApi, '/api/login')
    api.add_resource(TokenApi, '/api/token-chekcer')
    
    migrate.init_app(app, db)


    return app