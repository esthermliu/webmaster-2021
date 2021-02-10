from app import db # importing the database object
from app import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin # A class that Flask-Login provides with generic implementations that are typically appropriate for most user model classes

class User(UserMixin, db.Model): # inherits from db.Model, a base class for all models from Flask-SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True) # Username must be unique
    email = db.Column(db.String(120), index=True, unique=True) # Email must be unique
    password_hash = db.Column(db.String(128))

    def __repr__(self): # Tells Python how to print objects of this class
        return '<User {}>'.format(self.username)

    def set_password(self, password): # generates the password hash
        self.password_hash = generate_password_hash(password) 

    def check_password(self, password):
        return check_password_hash(self.password_hash, password) # checks the password hash with the actual password

@login.user_loader #Flask login needs the app's help in loading the user
def load_user(id): 
        return User.query.get(int(id))
