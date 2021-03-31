from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'thisismysecretkeydonotstealit'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
    app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.jpeg']
    app.config['UPLOAD_PATH'] = 'E:/Documents/diplomaDev/pneumonia-recognizer/recognizer-app/images/NORMAL'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from project.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from project.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app