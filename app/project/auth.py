import flask_login
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required,current_user

from .auth_services import signup_service, login_service
from .models import User
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    status = login_service(email, password, remember)
    if(status):
        return redirect(url_for('main.index'))
    else:
        return redirect(url_for('auth.login'))


@auth.route('/signup')
def signup():
    return render_template('signup.html')


def profil2e():
    print("Cur user ")
    print(str(flask_login.current_user.email))
    data =flask_login.current_user
    print(str(data))

    return render_template('profile.html', data=data )


#
@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    signup_service(email, name, password)
    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
