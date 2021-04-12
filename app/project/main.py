import flask_login
from flask import Blueprint, render_template
import os
from flask import Flask, render_template, request, redirect, url_for, abort, app
from werkzeug.utils import secure_filename

from .mynetwork import recognize_image
from .models import Image
from . import db

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




#
@main.route('/recognize', methods=['POST'])
def recognize_post():

    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    print(filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in ['.jpg', '.png', '.jpeg']:
            abort(400)
        # shutil.rmtree('E:/Documents/diplomaDev/pneumonia-recogognizer-app/app/project/images/NORMAL')
        uploaded_file.save(
            os.path.join('E:/Documents/diplomaDev/pneumonia-recogognizer-app/app/project/images/PNEUMONIA', filename))
        print("saved")
        user = flask_login.current_user
        print(uploaded_file)
        data = recognize_image()
        import base64
        data_uri = base64.b64encode(open('E:/Documents/diplomaDev/pneumonia-recogognizer-app/app/project/images/PNEUMONIA/'+filename, 'rb').read()).decode('utf-8')
        img_tag = '<img src="data:image/png;base64,{0}" width="450" height="450" alt="">'.format(data_uri)
        import uuid

        identifier = str(uuid.uuid4().fields[-1])[:5]
        import datetime
        today = datetime.datetime.today()
        date = today.strftime("%Y-%m-%d-%H.%M.%S")
        img = Image(img_tag,data['conclusion'],data['probability'],data['status'],data['result'],user.email,identifier,date)
        print( "id")

        print(img.identifier)


        db.session.add(img)
        db.session.commit()
        img2 = Image(img_tag,data['conclusion'],data['probability'],data['status'],data['result'],user.email,identifier,date)

        os.remove('E:/Documents/diplomaDev/pneumonia-recogognizer-app/app/project/images/PNEUMONIA/'+filename)
    return render_template('recognizer.html', data=img2)
ROWS_PER_PAGE = 2

#history.html
@main.route('/history')
def history():
    user = flask_login.current_user
    page = request.args.get('page', 1, type=int)
    data = Image.query.filter(Image.email == user.email).paginate(page=page, per_page=ROWS_PER_PAGE)
    # data = Image.query.filter(Image.email == user.email).all()
    print(history)
    return render_template('history.html', data=data)

@main.route('/recognize')
def recognize():
    return render_template('recognizer.html', data={})

#
# def recognize_image2():
#     image_size = 256
#     datagen = ImageDataGenerator(rescale=1. / 255)
#     from numpy.random import seed
#     seed(1)
#     model = load_model('E:/Documents/diplomaDev/pneumonia-recogognizer-app/app/project/my_model')
#     model.summary()
#     one_img = datagen.flow_from_directory(
#         'E:/Documents/diplomaDev/pneumonia-recogognizer-app/app/project/images',
#         target_size=(image_size, image_size),
#         color_mode="grayscale",
#         batch_size=1,
#         class_mode='binary')
#     y_pred = model.predict(one_img)
#     answer = y_pred > 0.5
#     print(y_pred > 0.5)
#     return answer
