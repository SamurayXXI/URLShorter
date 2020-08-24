import pytest

from shorter import db
from shorter.models import Link


@pytest.fixture(scope="function")
def app():
    from shorter.app import app
    from shorter import init_app
    application = init_app(app, "shorter.config.TestConfig")
    return application


def create_link(full_url, short="Qwe", counter=0):
    new_link = Link(short=short, full=full_url, follow_counter=counter)
    db.session.add(new_link)
    db.session.commit()