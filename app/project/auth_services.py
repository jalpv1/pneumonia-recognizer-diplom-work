import flask_login
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required,current_user
from .models import User
from . import db

def signup_service(email,name,password):
    user = User.query.filter_by(email=email).first()

    if user:
        flash('Email address already exists.')
        return redirect(url_for('auth.signup'))

    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()

def login_service(email,password,remember):
    user = User.query.filter_by(email=email).first()
    if user == None:
        flash('Please check your login details and try again.')
        return False
        #return redirect(url_for('auth.login'))
    if not user and not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return False
       # return redirect(url_for('auth.login'))

    login_user(user, remember=remember)
    return True