import os
from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from .db import db
from .post.view import post_blueprint

app = Flask(__name__)
CORS(app)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///' + os.path.join(basedir, 'data_sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app,db)

app.register_blueprint(post_blueprint)