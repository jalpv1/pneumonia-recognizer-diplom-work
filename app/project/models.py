from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class Image(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.String(1000))
    conclusion = db.Column(db.String(1000))
    probability = db.Column(db.String(1000))
    status = db.Column(db.String(1000))
    email = db.Column(db.String(1000))
    data = db.Column(db.String(1000))


    def __init__(self, data, conclusion,probability,status, result,email):
        self.data = data
        self.result = result
        self.conclusion = conclusion
        self.probability = probability
        self.status = status
        self.email = email

class Result:
    def __init__(self, conclusion,probability,status, result):
        self.result = result
        self.conclusion = conclusion
        self.probability = probability
        self.status = status
