import string
from random import choice

from shorter import app
from shorter.models import Link
from shorter.services import increment_url_size, get_link_size


def __create_link(size: int) -> str:
    """Create a random link with length 'size' """
    link = []
    for i in range(size):
        link.append(choice(string.ascii_letters + string.digits))
    return "".join(link)


def check_link_exists(short_url: str) -> bool:
    """Check short URL exists in database"""
    queryset = Link.query.filter_by(short=short_url).first()
    if queryset:
        return True
    return False


def create() -> str:
    """Create guaranteed new link not exists in database"""
    size = get_link_size()
    new_link = __create_link(size)
    tries = 0
    while check_link_exists(new_link):
        if tries < app.config["MAX_GENERATING_ATTEMPTS"]:
            tries += 1
        else:
            increment_url_size()
            tries = 0

        new_link = __create_link(get_link_size())

    return new_link
