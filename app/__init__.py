from flask import Flask
from app.db import db
from app.routes import todo_bp
from app.models import ToDoTable

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.register_blueprint(todo_bp)
    return app
