from shorter.models import Link
from shorter.services import get_short_link, set_follow_counter, get_url_follows
from .common_fixtures import app, create_link


def test_create_short_url(app):
    app_client = app.test_client()
    yandex_url = "https://yandex.ru/"
    google_url = "https://www.google.com/"
    app_client.post('/', data={"url": yandex_url})
    app_client.post('/', data={"url": yandex_url})
    app_client.post('/', data={"url": google_url})
    app_client.post('/', data={"url": google_url})

    with app.app_context():
        links = Link.query.all()
        assert len(links) == 2
        yandex_short = get_short_link(yandex_url)
        google_short = get_short_link(google_url)
        assert yandex_short != google_short


def test_root_follows(app):
    app_client = app.test_client()
    full_url = "https://yandex.ru/"
    app_client.post('/', data={"url": full_url})
    with app.app_context():
        set_follow_counter(full_url, 2)
    rv = app_client.post('/', data={"url": full_url})
    assert "Follows: 2" in str(rv.data)


def test_increment_follows(app):
    app_client = app.test_client()
    full_url = "https://yandex.ru/"
    with app.app_context():
        create_link(full_url)
        app_client.get('/Qwe')
        app_client.get('/Qwe')
        assert get_url_follows(full_url) == 2
