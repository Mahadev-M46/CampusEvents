from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    date = db.Column(db.Date, nullable=False)  # Changed to db.Date
    location = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.Date, default=date.today)   # Pass function, not result

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "date": self.date.isoformat() if self.date else None,
            "location": self.location,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }