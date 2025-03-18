from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired , EqualTo, Length, Email

class RegisterForm(FlaskForm):
    userName= StringField("UserName", validators=[DataRequired()])
    email= StringField("Email",validators=[DataRequired(),Email()])
    phone= StringField("Phone",validators=[DataRequired(),Length(min=11,max=11)])
    password= PasswordField("Password",validators=[DataRequired(),Length(min=6)])
    confirm_password=PasswordField("Confirm Password",validators=[DataRequired(),EqualTo('password')])
    btn= SubmitField("Sign Up")

class LoginForm(FlaskForm):
    email= StringField("Email",validators=[DataRequired(),Email()])
    password= PasswordField("Password",validators=[DataRequired(),Length(min=6)])
    remember_me= BooleanField("Remember Me")
    btn=SubmitField("Login")