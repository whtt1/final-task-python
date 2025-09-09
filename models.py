from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()


class PhoneNumber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String, unique=True, nullable=False)
    check_count = db.Column(db.Integer, default=0)
    valid = db.Column(db.Boolean, default=False)
    comments = db.relationship('Comment', backref='phone_number')


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(12), unique=True, nullable=True)
    password = db.Column(db.String, nullable=False)
    is_confirmed = db.Column(db.Boolean, default=False)
    network = db.Column(db.String, nullable=True)
    comments = db.relationship('Comment', backref='user')


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    phone_number_id = db.Column(db.Integer, db.ForeignKey('phone_number.id'), nullable=False)
