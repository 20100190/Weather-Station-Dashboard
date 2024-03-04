from time import time
from datetime import datetime
from app import db

class BasicInfo(db.Model):
    """1.1 Weather Data"""
    __tablename__ = "weather_data"
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Date, nullable=True)
    city = db.Column(db.String(100))
    data = db.Column(db.JSON)

    def __repr__(self):
        return f"<1.1 Weather Data ({self.id}) {self.time}>"
