import os
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig(object):
    DEBUG = False
    
    SECRET_KEY = "abcdefghijklmnopqrstuvwxyz"

    SECURITY_PASSWORD_SALT = "dontbesaltybuddy"


class DevConfig(BaseConfig):
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or f"sqlite:///{os.path.join(basedir, 'app.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(BaseConfig):
    SECRET_KEY = os.environ.get("SECRET_KEY") or config.get("configs", "SECRET_KEY")