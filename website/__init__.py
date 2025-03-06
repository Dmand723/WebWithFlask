from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from os import getenv,path
from flask_login import LoginManager

load_dotenv()

db = SQLAlchemy()
DB_NAME = 'flaskDB.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    
    from .veiws import veiws
    from .auth import auth

    app.register_blueprint(veiws, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User,Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    return app 

def create_database(app):
    if not path.exists(DB_NAME):
        with app.app_context():
            db.create_all()
        print("Created Database!")

#1:55:00