from flask import Flask
from config import DevConfig, ProdConfig

app = Flask(__name__)

app.config.from_object(DevConfig)
#app.config.from_object(ProdConfig)

from app import routes
