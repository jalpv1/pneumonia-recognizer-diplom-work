import flask_login
from flask import Blueprint, render_template, flash
import os
from flask import Flask, render_template, request, redirect, url_for, abort, app
from werkzeug.utils import secure_filename

from .mynetwork import recognize_image
from .models import Image
from . import db

def recognize_service(uploaded_file):
    filename = secure_filename(uploaded_file.filename)
    print(filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in ['.jpg', '.png', '.jpeg']:
            flash('Wrong file extension. Supported extensions: .jpg ,.png,.jpeg')
        else:
            uploaded_file.save(
                os.path.join('E:/Documents/diplomaDev/pneumonia-recogognizer-app/app/project/images/PNEUMONIA',
                             filename))
            print("saved")
            user = flask_login.current_user
            print(uploaded_file)
            data = recognize_image()
            import base64
            data_uri = base64.b64encode(
                open('E:/Documents/diplomaDev/pneumonia-recogognizer-app/app/project/images/PNEUMONIA/' + filename,
                     'rb').read()).decode('utf-8')
            img_tag = '<img src="data:image/png;base64,{0}" width="450" height="450" alt="">'.format(data_uri)
            import uuid

            identifier = str(uuid.uuid4().fields[-1])[:5]
            import datetime
            today = datetime.datetime.today()
            date = today.strftime("%Y-%m-%d-%H.%M.%S")
            img = Image(img_tag, data['conclusion'], data['probability'], data['status'], data['result'], user.email,identifier, date)
            db.session.add(img)
            db.session.commit()
            img2 = Image(img_tag, data['conclusion'], data['probability'], data['status'], data['result'], user.email, identifier, date)
            os.remove('E:/Documents/diplomaDev/pneumonia-recogognizer-app/app/project/images/PNEUMONIA/' + filename)
            return img2


def history_service(rows):
    user = flask_login.current_user
    page = request.args.get('page', 1, type=int)
    data = Image.query.filter(Image.email == user.email).paginate(page=page, per_page=rows)
    return data