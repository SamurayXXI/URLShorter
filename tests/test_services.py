import string

import pytest
from pytest import raises

from shorter import db, url_maker
from shorter.models import Link
from shorter.services import check_exists_url, get_url_hits, short_url


@pytest.fixture(scope="session")
def app():
    from shorter.app import app
    from shorter import init_app
    application = init_app(app, "shorter.config.TestConfig")
    return application


@pytest.fixture(scope="session")
def all_links_size_1():
    from shorter.app import app
    from shorter import init_app
    application = init_app(app, "shorter.config.TestConfig")
    with application.app_context():
        application.config["MIN_LINK_SIZE"] = 1
        for char in string.ascii_letters + string.digits:
            link = Link(short=char, full=f"Qwe{char}", counter=1)
            db.session.add(link)
        db.session.commit()

    return application


def create_link(full_url, counter=1):
    new_link = Link(short="Qwe", full=full_url, counter=counter)
    db.session.add(new_link)
    db.session.commit()


def delete_link(full_url):
    Link.query.filter_by(full=full_url).delete()
    db.session.commit()


def check_links_is_empty():
    if Link.query.all():
        return False
    return True


def test_check_exists_url(app):
    with app.app_context():
        full_url = "https://yandex.ru/"
        assert check_links_is_empty()
        assert not check_exists_url(full_url)
        create_link(full_url)
        assert check_exists_url(full_url)
        delete_link(full_url)
        assert not check_exists_url(full_url)


def test_get_url_hints(app):
    with app.app_context():
        full_url = "https://yandex.ru/"
        assert check_links_is_empty()
        with raises(AttributeError):
            get_url_hits(full_url)
        create_link(full_url, 21)
        link = Link.query.filter_by(short="Qwe").first()
        assert link.counter == 21


def test_create_link(all_links_size_1):
    with all_links_size_1.app_context():
        url = url_maker.create()
        assert len(url) > 1


def test_create_short_url(app):
    with app.app_context():
        yandex_url = "https://yandex.ru/"
        google_url = "https://www.google.com/"
        short_yandex_1 = short_url(yandex_url)
        short_yandex_2 = short_url(yandex_url)
        short_google_1 = short_url(google_url)
        short_google_2 = short_url(google_url)
        assert short_yandex_1 == short_yandex_2
        assert short_google_1 == short_google_2
        assert short_yandex_1 != short_google_1
