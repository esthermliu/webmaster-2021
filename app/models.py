from app import db # importing the database object
from app import login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin # A class that Flask-Login provides with generic implementations that are typically appropriate for most user model classes
from time import time
import jwt
from app import app
from datetime import datetime

class User(UserMixin, db.Model): # inherits from db.Model, a base class for all models from Flask-SQLAlchemy
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True) # Username must be unique
    email = db.Column(db.String(120), index=True, unique=True) # Email must be unique
    password_hash = db.Column(db.String(128))
    first_name = db.Column(db.String(64), index=False, unique=False)
    last_name = db.Column(db.String(64), index=False, unique=False)
    phone = db.Column(db.String(64), index=True, unique=True)
    gender = db.Column(db.Integer, index=False, unique=False)
    birthday = db.Column(db.DateTime, index=False, unique=False)
    address = db.Column(db.String(128), index=False, unique=False)
    city = db.Column(db.String(64))
    state = db.Column(db.Integer)
    zip_code = db.Column(db.Integer)
    appointments = db.relationship('Appointments', backref='patient', lazy='dynamic')
    allergies = db.relationship('Allergies', backref='patient_allergy', lazy='dynamic')
    surgeries = db.relationship('Surgeries', backref='patient_surgery', lazy='dynamic')
    conditions = db.relationship('Conditions', backref='patient_condition', lazy='dynamic')

    def __repr__(self): # Tells Python how to print objects of this class
        return '<User {}>'.format(self.username)

    def set_password(self, password): # generates the password hash
        self.password_hash = generate_password_hash(password) 

    def check_password(self, password):
        return check_password_hash(self.password_hash, password) # checks the password hash with the actual password

    def get_reset_password_token(self, expires_in=600): # returns a JWT token as a string
        return jwt.encode( # Encodes the user's id
            {'reset_password': self.id, 'exp': time() + expires_in},
            app.config['SECRET_KEY'], algorithm='HS256')

    @staticmethod 
    def verify_reset_password_token(token): # attempts to decode the token
        try: 
            id = jwt.decode(token, app.config['SECRET_KEY'],
                                    algorithms=['HS256'])['reset_password']
        except: # if token is not valid or is expired, then None is returned
            return
        return User.query.get(id) # otherwise, if token is valid, then return the user through the decoded token, which returns the user's id

@login.user_loader #Flask login needs the app's help in loading the user
def load_user(id): 
        return User.query.get(int(id))

class Appointments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    start_time = db.Column(db.DateTime, index=True)
    end_time = db.Column(db.DateTime, index=True)
    description = db.Column(db.String(220))
    doctor = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Appointments {} {} {}>'.format(self.id, self.user_id, self.timestamp)

class Allergies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    allergy = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Allergies {} {} {}>'.format(self.id, self.user_id, self.allergy)

class Surgeries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    surgery = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Surgeries {} {} {}>'.format(self.id, self.user_id, self.surgery)

class Conditions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    condition = db.Column(db.String(200))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Conditions {} {} {}>'.format(self.id, self.user_id, self.condition)