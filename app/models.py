from app import db

class User(db.Model):  # UpperCamelCase for model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='pending')
