from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Tariff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.Time)
    end_time = db.Column(db.Time)
    price = db.Column(db.Float)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    notified = db.Column(db.Boolean, default=False)
