from ensurepip import bootstrap
from flask import Flask
from .config import DevConfig
from app import views
from flask_bootstrap import Bootstrap
# Initializing application
app = Flask(__name__,instance_relative_config=True)

# Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

bootstrap=Bootstrap(app)

