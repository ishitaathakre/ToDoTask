from app.db import db

class ToDoTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(256), nullable=False)
    status = db.Column(db.String(50), default="Pending")
