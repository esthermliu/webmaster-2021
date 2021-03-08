from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateTimeField, SelectField, DateField, TextAreaField, RadioField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User
from datetime import date

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()]) # Optional validators, used to attach validation behaviors to fields, makes sure that the field is not submitted empty
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[(0, 'Male'), (1, 'Female'), (2, 'Other')], coerce=int)
    address = StringField('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = SelectField('State', choices=[(0, 'Alabama'), (1, 'Alaska')], coerce=int)
    zip_code = IntegerField('ZIP', validators=[DataRequired()])
    datepicker = DateField('Birthday', format='%m/%d/%Y', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')]) # checking whether this re-entered password is equal to the first password
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('This username is already taken.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('This email address is already taken.')

class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')

class MakeAppointmentForm(FlaskForm):
    datepicker = DateField('Date', format='%m/%d/%Y', validators=[DataRequired()])
    hour = SelectField('Hour', choices=[(1, '1 AM'),(2, '2 AM'),(3, '3 AM'),(4, '4 AM'),(5, '5 AM'),(6, '6 AM'),(7, '7 AM'),(8, '8 AM'),(9, '9 AM'),
                                        (10, '11 AM'),(12, '12 PM'),(13, '1 PM'),(14, '2 PM'),(15, '3 PM'),(16, '4 PM'),(17, '5 PM'),(18, '6 PM'),
                                        (19, '7 PM'),(20, '8 PM'),(21, '9 PM'),(22, '10 PM'),(23, '11 PM'),(0, '12 AM'),
                                        ],
                                        coerce=int)
    minute = SelectField('Minutes', choices=[(0, '00'),(15, '15'), (30, '30'), (45, '45')], coerce=int)
    duration = SelectField('Meeting Duration', choices=[(30, '30 mins'), (45, '45 mins'), (60, '1 hr'), (90, '1.5 hr'), (120, '2 hr')], coerce=int)
    description = TextAreaField('Description of Problem', validators=[Length(min=0, max=140)])
    doctor = SelectField('Select Doctor', choices=[(0, 'Sammy Urtzal'), (1, 'Peyton Everlue'), (2, 'Joselyn Sputak')], coerce=int)
    consent = BooleanField('By clicking you consent for treatment', validators=[DataRequired()])
    submit = SubmitField('Make Appointment')

class UserAccount(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    gender = SelectField('Gender', choices=[(0, 'Male'), (1, 'Female'), (2, 'Other')], coerce=int)
    address = StringField('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = SelectField('State', choices=[(0, 'Alabama'), (1, 'Alaska'), (2, 'Arizona'), (3, 'Arkansas'), (4, 'California'),
                                            (5, 'Colorado'), (6, 'Connecticut'), (7, 'Delaware'), (8, 'Florida'), (9, 'Georgia'),
                                            (10, 'Hawaii'), (11, 'Idaho'), (12, 'Illinois'), (13, 'Indiana'), (14, 'Iowa'),
                                            (15, 'Kansas'), (16, 'Kentucky'), (17, 'Louisiana'), (18, 'Maine'), (19, 'Maryland'),
                                            (20, 'Massachusetts'), (21, 'Michigan'), (22, 'Minnesota'), (23, 'Mississippi'),
                                            (24, 'Missouri'), (25, 'Montana'), (26, 'Nebraska'), (27, 'Nevada'), (28, 'New Hampshire'),
                                            (29, 'New Jersey'), (30, 'New Mexico'), (31, 'New York'), (32, 'North Carolina'), (33, 'North Dakota'),
                                            (34, 'Ohio'), (35, 'Oklahoma'), (36, 'Oregon'), (37, 'Pennsylvania'), (38, 'Rhode Island'),
                                            (39, 'South Carolina'), (40, 'South Dakota'), (41, 'Tennessee'), (42, 'Texas'), (43, 'Utah'),
                                            (44, 'Vermont'), (45, 'Virginia'), (46, 'Washington'), (47, 'West Virginia'), (48, 'Wisconsin'),
                                            (49, 'Wyoming')], coerce=int)
    zip_code = IntegerField('ZIP', validators=[DataRequired()])
    submit = SubmitField('Save')

class AllergyForm(FlaskForm):
    allergy = StringField('Allergy', validators=[DataRequired()])
    submit = SubmitField('Add Allergen')

class SurgeryForm(FlaskForm):
    surgery = StringField('Surgery', validators=[DataRequired()])
    submit = SubmitField('Add Surgery')

class ConditionForm(FlaskForm):
    condition = StringField('Condition', validators=[DataRequired()])
    submit = SubmitField('Add Medical Condition')