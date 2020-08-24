import string

import pytest
from pytest import raises

from shorter import db, url_maker
from shorter.models import Link
from shorter.services import check_exists_url, get_url_follows, get_full_link_by_short, set_follow_counter, \
    increment_follow_counter
from .common_fixtures import app, create_link


@pytest.fixture(scope="function")
def all_links_size_1():
    from shorter.app import app
    from shorter import init_app
    application = init_app(app, "shorter.config.TestConfig")
    with application.app_context():
        application.config["MIN_LINK_SIZE"] = 1
        for char in string.ascii_letters + string.digits:
            link = Link(short=char, full=f"Qwe{char}", follow_counter=1)
            db.session.add(link)
        db.session.commit()

    return application


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


def test_get_url_follows(app):
    with app.app_context():
        full_url = "https://yandex.ru/"
        assert check_links_is_empty()
        with raises(AttributeError):
            get_url_follows(full_url)
        create_link(full_url, counter=21)
        link = Link.query.filter_by(short="Qwe").first()
        assert link.follow_counter == 21


def test_create_link(all_links_size_1):
    with all_links_size_1.app_context():
        url = url_maker.create()
        assert len(url) > 1


def test_get_full_link_by_short(app):
    full_url = "https://yandex.ru/"
    with app.app_context():
        create_link(full_url)
        assert get_full_link_by_short("Qwe") == full_url
        assert get_full_link_by_short("Qwqsdfg") == ""


def test_increment_follows(app):
    full_url = "https://yandex.ru/"
    with app.app_context():
        create_link(full_url)
        set_follow_counter(full_url, 10)
        increment_follow_counter("Qwe")
        assert get_url_follows(full_url) == 11
