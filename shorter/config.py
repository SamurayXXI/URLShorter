import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DB_CONNECTION")
    WTF_CSRF_ENABLED = False
    MIN_LINK_SIZE = 3
    MAX_GENERATING_ATTEMPTS = 10
    DEBUG = True


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"