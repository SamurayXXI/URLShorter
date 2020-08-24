from flask import render_template

from shorter import app
from shorter.forms import URLForm
from shorter.services import check_exists_url, get_url_follows, create_new_url, get_short_link_with_domain, \
    wrap_link_with_domain, save_new_url


@app.route('/', methods=['get', 'post'])
def index():
    form = URLForm()
    if form.validate_on_submit():
        full_url = form.url.data
        if check_exists_url(full_url):
            return render_template('index.html', form=form,
                                   short_url=get_short_link_with_domain(full_url),
                                   follows=get_url_follows(full_url))

        new_url = create_new_url()
        save_new_url(full_url, new_url)
        return render_template('index.html', form=form,
                               short_url=wrap_link_with_domain(new_url))

    return render_template('index.html', form=form)


