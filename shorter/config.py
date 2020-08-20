import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DB_CONNECTION")
    WTF_CSRF_ENABLED = False