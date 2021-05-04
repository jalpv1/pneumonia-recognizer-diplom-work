import flask_login
from flask import Blueprint
from flask import Flask, render_template, request
from .main_services import recognize_service, history_service


main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
def profile():
    print("Cur user ")
    print(str(flask_login.current_user.email))
    data =flask_login.current_user
    print(str(data))

    return render_template('profile.html', data=data )

@main.route('/recognize', methods=['POST'])
def recognize_post():
    uploaded_file = request.files['file']
    img2 = recognize_service(uploaded_file);
    return render_template('recognizer.html', data=img2)
ROWS_PER_PAGE = 2

@main.route('/history')
def history():
    data = history_service(ROWS_PER_PAGE)
    return render_template('history.html', data=data)

@main.route('/recognize')
def recognize():
    return render_template('recognizer.html', data={})