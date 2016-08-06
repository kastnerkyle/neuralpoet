"""
Neural Poet
===========
"""
import os

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_cors import CORS
from flask_heroku import Heroku

from .views.site import site

__title__ = 'neuralpoet'
__license__ = 'Apache Software License Version 2.0'

app = Flask(__name__, instance_relative_config=True)


app.register_blueprint(site)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config.from_object(os.environ['APP_SECRET'])

# Enable CORS Configuration
cors = CORS(app)
bootstrap = Bootstrap(app)
heroku = Heroku(app)
