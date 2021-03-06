from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .model import History
    from .route import views
    app.register_blueprint(views, url_prefix='/')

    create_database(app)
    return app


def create_database(app):
    if not path.exists('project/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')