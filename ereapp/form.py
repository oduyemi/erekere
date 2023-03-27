from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, length, Regexp
from ereapp.models import User, Admin, Contact

    


class LoginForm(FlaskForm):
    username = StringField("username",
        validators=
            [DataRequired(),
            length(min=1, max=40),
            Regexp('[a-z0-9]+@[a-z]+.[a-z]{2,3}', 0, "Please provide a valid username")],
            render_kw={"placeholder": "Username"})
    
    password = PasswordField("password",
        validators=
            [DataRequired(),
            length(min=5, max=20)],
            render_kw={"placeholder": "Enter your password"})
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")


class SignUp(FlaskForm):
    fullname = StringField("fullname",
        validators=
            [DataRequired(),
            length(min=5, max=100),
            Regexp('[a-z0-9]+@[a-z]+.[a-z]{2,3}', 0, "Please provide a valid name")],
            render_kw={"placeholder": "Fullname"})
    phone = StringField("email",
        validators=
            [DataRequired(),
            length(min=5, max=40),
            Regexp('[a-z0-9]+@[a-z]+.[a-z]{2,3}', 0, "Please provide a valid email address")],
            render_kw={"placeholder": "Phone Number"})
    username = StringField("email",
        validators=
            [DataRequired(),
            length(min=5, max=30),
            Regexp('[a-z0-9]+@[a-z]+.[a-z]{2,3}', 0, "Please provide a valid email address")],
            render_kw={"placeholder": "Email address"})
    password = PasswordField("password",
        validators=
            [DataRequired(),
            length(min=5, max=20)],
            render_kw={"placeholder": "Enter your password"})
    remember = BooleanField("Remember Me")
    submit = SubmitField("Login")
