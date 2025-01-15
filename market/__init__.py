from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():

    app = Flask(__name__)


    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.db"

    db.init_app(app)


    with app.app_context():
        from market import routes
        from market.models import User, Item
        db.create_all()

    return app

app = create_app()
