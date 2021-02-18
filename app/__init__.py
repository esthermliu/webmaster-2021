from flask import Flask, request # Creates app as an instance of class Flask imported from the flask package
from flaskext.markdown import Markdown
from config import Config # lowercase config is the name of the Python module and the uppercase is the actual class
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__) # __name__ is a Python predefined variable, set to the name of the module in which it is used
Markdown(app) 
app.config.from_object(Config)  
db = SQLAlchemy(app) # this db object represents the database
migrate = Migrate(app, db, render_as_batch=True) # this object represents the migration engine
login = LoginManager(app)
login.login_view = 'login'
mail = Mail(app)

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    moment.init_app(app)

    return app

from app import routes, models # Importing the routes module, imported at the bottom to avoid circular imports, also imports models module
