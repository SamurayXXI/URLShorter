from shorter import db


class Link(db.Model):
    short = db.Column(db.String(24), primary_key=True)
    full = db.Column(db.Text, unique=True, nullable=False)
    counter = db.Column(db.Integer)


class Settings(db.Model):
    name = db.Column(db.String(12), primary_key=True)
    value = db.Column(db.Integer)
