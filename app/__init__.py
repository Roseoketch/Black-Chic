from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_mail import Mail
from flask_moment import Moment

#login Configurations
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
# login_manager.session_protection attribute provides different security levels and by setting it to strong will monitor changes in a user's request header and log the user out

#Configurations
bootstrap = Bootstrap()
db = SQLAlchemy()
"""
Main configurations class
"""
photos = UploadSet('photos', IMAGES)
mail = Mail()
moment = Moment()

def create_app(config_name):
   # Initializing the app instance
   app = Flask(__name__)

   # Creating the app configurations
   app.config.from_object(config_options[config_name])

   # configure UploadSet
   configure_uploads(app,photos)


   # Initializing flask extensions
   bootstrap.init_app(app)
   db.init_app(app)
   moment.init_app(app)
   login_manager.init_app(app)
   # simple.init_app(app)
   configure_uploads(app,photos)
   mail.init_app(app)

   #Registrating the blueprint
   from .main import main as main_blueprint
   app.register_blueprint(main_blueprint)

   from .auth import auth as auth_blueprint
   app.register_blueprint(auth_blueprint, url_prefix = '/authenticate')

   return app
