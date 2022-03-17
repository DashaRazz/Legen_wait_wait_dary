from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from os import path
from config import Config
from flask_login import LoginManager

db = SQLAlchemy()


app = Flask(__name__)
app.config['SECRET_KEY'] = 'neotchislyaitemenyapozhaluista'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///forum.db'
db.init_app(app)
from .views import views
from .auth import auth
app.register_blueprint(auth, url_prefix='/')
app.register_blueprint(views, url_prefix='/')

login = LoginManager(app)
login.login_view = 'auth.login'

from .models import User, Article, Status, Comment

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


if not path.exists('Forum/app/forum.db'):
    db.create_all(app=app)
