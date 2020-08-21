from shorter import db, app
from shorter.models import Link, Settings


def check_exists_url(full_url: str) -> bool:
    link = Link.query.filter_by(full=full_url).first()
    if link:
        return True
    return False


def get_short_link(full_url: str) -> str:
    link = Link.query.filter_by(full=full_url).first()
    return link.short


def get_url_hints(full_url: str) -> int:
    link = Link.query.filter_by(full=full_url).first()
    return link.counter


def create_new_url() -> str:
    from shorter import url_maker
    return url_maker.create()


def save_new_url(full_url: str, new_url: str) -> None:
    link = Link(short=new_url, full=full_url, counter=0)
    db.session.add(link)
    db.session.commit()


def short_url(full_url: str) -> str:
    if check_exists_url(full_url):
        return get_short_link(full_url)

    new_url = create_new_url()
    save_new_url(full_url, new_url)
    return new_url


def get_link_size() -> int:
    size = Settings.query.filter_by(name="current_link_size").first()
    if size:
        return size.value
    return app.config["MIN_LINK_SIZE"]


def increment_url_size() -> None:
    size = Settings.query.filter_by(name="current_link_size").first()
    if size:
        size.value += 1
        db.session.commit()
    else:
        current_link_setting = Settings(name="current_link_size", value=get_link_size()+1)
        db.session.add(current_link_setting)
        db.session.commit()
