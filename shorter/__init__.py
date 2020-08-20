from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("shorter.config.Config")
db = SQLAlchemy(app)

from shorter.models import Link, Settings
db.create_all()
