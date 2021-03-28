import flask_login
from flask import Blueprint, render_template
import os
from flask import Flask, render_template, request, redirect, url_for, abort, app
from werkzeug.utils import secure_filename
from keras.models import load_model
from keras_preprocessing.image import ImageDataGenerator
import shutil
from flask_login import login_user, logout_user, login_required,current_user

from .mynetwork import recognize_image
from .models import Image

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
        # shutil.rmtree('E:/Documents/diplomaDev/pneumonia-recogognizer-app/app/project/images/one')
        uploaded_file.save(
            os.path.join('E:/Documents/diplomaDev/pneumonia-recogognizer-app/app/project/images/one', filename))
        print("saved")
        print(uploaded_file)
        data = recognize_image()
        import base64
        data_uri = base64.b64encode(open('E:/Documents/diplomaDev/pneumonia-recogognizer-app/app/project/images/one/'+filename, 'rb').read()).decode('utf-8')
        img_tag = '<img src="data:image/png;base64,{0}" width="300" height="450" alt="">'.format(data_uri)
        img = Image(img_tag,data['conclusion'],data['probability'],data['status'],data['result'])
        print(img.result)
        print(img.status)
        print(img.probability)
        print(img.conclusion)

        os.remove('E:/Documents/diplomaDev/pneumonia-recogognizer-app/app/project/images/one/'+filename)
    return render_template('recognizer.html', data=img)


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
