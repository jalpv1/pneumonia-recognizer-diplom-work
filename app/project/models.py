from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class Image:
    def __init__(self, data, conclusion,probability,status, result):
        self.data = data
        self.result = result
        self.conclusion = conclusion
        self.probability = probability
        self.status = status

class Result:
    def __init__(self, conclusion,probability,status, result):
        self.result = result
        self.conclusion = conclusion
        self.probability = probability
        self.status = status
