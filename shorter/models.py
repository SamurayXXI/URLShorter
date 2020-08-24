from shorter import db


class Link(db.Model):
    short = db.Column(db.String(24), primary_key=True)
    full = db.Column(db.Text, nullable=False, unique=True)
    follow_counter = db.Column(db.Integer)


class Settings(db.Model):
    """Contains a current url size"""
    name = db.Column(db.String(12), primary_key=True)
    value = db.Column(db.Integer)
