from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

def key():
    return "Dasha"

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        nickname = request.form.get('nickname')
        email = request.form.get('email')
        password = request.form.get('password')


    #filter_by работает как то, что мы ищем всех пользователей в бд с данным email, first выводит первого юзера
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
                login_user(user, remember=True)
                redirect(url_for("index"))
            else:
                flash("Incorrect password", category="error")
        else:
            flash("email does not exist", category="error")


    return render_template("login.html", user=current_user)


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method=="POST":
        print("НАЧАЛИ")
        email = request.form.get("email")
        print("НАЧАЛИ1")
        nickname = request.form.get("nickname")
        print("НАЧАЛИ2")
        password1 = request.form.get("password1")
        print("НАЧАЛИ3")
        password2 = request.form.get("password2")
        print("НАЧАЛИ4")

        user = User.query.filter_by(email=email).first()
        if user:
            flash("Hey, bro, user is already exist",category='error')
        elif len(email) < 4:
            flash("Email must be greater than 4 characters.", category='error')

        elif password1 != password2:
            flash("Passwords don't match.", category='error')

        elif len(password1) < 6:
            flash("Password must be at least 6 characters.", category='error')
        elif len(nickname) < 2:
            flash("Nicname не работает")

        else:
            # add user to database
            new_user=User(nickname=nickname, email=email, password=generate_password_hash(password1, method="sha256"))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            user=current_user
            flash("Accout created! Let's say hello to this world!", category="success")


            return redirect(url_for("index"))


    return render_template("sign-up.html")
