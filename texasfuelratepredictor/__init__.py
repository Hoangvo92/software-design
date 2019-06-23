from flask import Flask
from flask_sqlalchemy import SQLAlchemy # see https://tinyurl.com/y65ko6h3
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from texasfuelratepredictor.config import Config
import os.path


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

def create_app(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from texasfuelratepredictor.users.routes import users
    from texasfuelratepredictor.main.routes import main
    from texasfuelratepredictor.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app

