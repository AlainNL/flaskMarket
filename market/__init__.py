import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
load_dotenv()


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Configurer la base de données
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.db"
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    db.init_app(app)

    # Enregistrer le Blueprint
    from market.routes import main
    app.register_blueprint(main)
    migrate.init_app(app, db)

    # Créer les tables après avoir configuré l'application
    with app.app_context():
        from market.models import User, Item
        db.create_all()

    return app


# Créer l'application
app = create_app()
