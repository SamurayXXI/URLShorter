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


def get_url_follows(full_url: str) -> int:
    link = Link.query.filter_by(full=full_url).first()
    return link.follow_counter


def set_follow_counter(full_url: str, count: int) -> None:
    link = Link.query.filter_by(full=full_url).first()
    link.follow_counter = count
    db.session.commit()


def create_new_url() -> str:
    from shorter import url_maker
    return url_maker.create()


def save_new_url(full_url: str, new_url: str) -> None:
    link = Link(short=new_url, full=full_url, follow_counter=0)
    db.session.add(link)
    db.session.commit()


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
        current_link_setting = Settings(
            name="current_link_size", value=get_link_size()+1)
        db.session.add(current_link_setting)
        db.session.commit()


def wrap_link_with_domain(url: str) -> str:
    domain = app.config.get("DOMAIN_NAME", "localhost")
    port = app.config.get("DOMAIN_PORT", 5000)
    link = f"http://{domain}:{port}/{url}"
    return link


def get_short_link_with_domain(url: str) -> str:
    return wrap_link_with_domain(get_short_link(url))


def get_full_link_by_short(url: str) -> str:
    link = Link.query.filter_by(short=url).first()
    if link:
        return link.full
    return ""


def increment_follow_counter(short_url: str) -> None:
    link = Link.query.filter_by(short=short_url).first()
    link.follow_counter += 1
    db.session.commit()
