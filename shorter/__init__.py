from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy()


def init_app(application, config=None):
    if not config:
        application.config.from_object("shorter.config.Config")
    else:
        application.config.from_object(config)
    db.init_app(application)

    from shorter.models import Link, Settings

    with application.app_context():
        db.create_all()

    return application

