from . import db


class Search(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(255), nullable=False)
    timestamp = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    data = db.Column(db.JSON, nullable=False)
