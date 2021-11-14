from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

basedir = os.path.abspath(os.path.dirname(__file__))
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['playerdna4@gmail.com']


app = Flask(__name__)

if not app.debug:
    config = Config()
    if hasattr(config, 'MAIL_SERVER'):
        auth = None
        if hasattr(config, 'MAIL_USERNAME') or hasattr(config, 'MAIL_PASSWORD'):
            auth = (getattr(config, 'MAIL_USERNAME'), hasattr(config, 'MAIL_USERNAME'))
        secure = () if hasattr(config, 'MAIL_USE_TLS') else None
        mail_handler = SMTPHandler(
            mailhost=(getattr(config, 'MAIL_SERVER'),  getattr(config, 'MAIL_PORT')),
            fromaddr='no-reply@' + getattr(config, 'MAIL_SERVER'),
            toaddrs=getattr(config, 'ADMINS'), subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')

login = LoginManager(app)
login.login_view = 'login'
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models, errors