from flask_wtf import FlaskForm
from ToDo.models import User
from wtforms import StringField, BooleanField, SubmitField,PasswordField
from wtforms.validators import DataRequired,EqualTo,Length,Email,ValidationError

class LoginForm(FlaskForm):
    email= StringField("Email",validators=[DataRequired(),Email()])
    password= PasswordField("Password",validators=[DataRequired(),Length(min=6)])
    remember_me= BooleanField("Remember Me")
    btn=SubmitField("Login")

class RegisterForm(FlaskForm):
    name= StringField("Username", validators=[DataRequired()])
    email= StringField("Email",validators=[DataRequired(),Email()])
    phone= StringField("Phone",validators=[DataRequired(),Length(min=11,max=11)])
    password= PasswordField("Password",validators=[DataRequired(),Length(min=6)])
    confirm_password=PasswordField("Confirm Password",validators=[DataRequired(),EqualTo('password')])
    btn= SubmitField("Sign Up")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Email is already exists")

    def validate_phone(self, phone):
        user = User.query.filter_by(phone=phone.data).first()
        if user:
            raise ValidationError("Phone is already exists")