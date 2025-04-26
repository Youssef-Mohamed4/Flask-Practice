from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY']= "kcladffaewq"
app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///database.db"

db=SQLAlchemy(app)
bcrypt = Bcrypt(app)
loginManager = LoginManager(app)
loginManager.login_view = "users.login"

from ToDo.main.routes import main
from ToDo.users.routes import users
from ToDo.tasks.routes import task

app.register_blueprint(main)
app.register_blueprint(users)
app.register_blueprint(task)