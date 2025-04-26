from flask import Blueprint, redirect,render_template,flash,url_for
from ToDo.users.forms import LoginForm,RegisterForm
from ToDo.models import User
from ToDo import db, bcrypt
from flask_login import current_user,login_required,login_user,logout_user

users = Blueprint("users", __name__)

@users.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password_hash, form.password.data):
            login_user(user, remember=form.remember.data)
            flash(f"Welcome {user.name}", "success")
            return redirect(url_for("home"))
        else:
            flash(f"Invalid Credentials", "danger")
    return render_template("login.html", title="login", form=form)

@users.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(name=form.name.data,phone=form.phone.data,
                    email=form.email.data,password_hash=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f"Account created for {form.name.data}", "success")
        return redirect(url_for("login"))
    return render_template("register.html", title="register", form=form)

@users.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))