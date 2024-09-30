from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String, nullable=False)
    short_id = db.Column(db.String, unique=True, nullable=False)


