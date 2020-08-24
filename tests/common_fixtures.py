import pytest


@pytest.fixture(scope="function")
def app():
    from shorter.app import app
    from shorter import init_app
    application = init_app(app, "shorter.config.TestConfig")
    return application
