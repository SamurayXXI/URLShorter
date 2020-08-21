from flask import render_template

from shorter import app
from shorter.forms import URLForm
from shorter.services import check_exists_url


@app.route('/', methods=['get', 'post'])
def index():
    form = URLForm()
    if form.validate_on_submit():
        print(form.url.data)
        print(check_exists_url("https://flask.palletsprojects.com/en/1.1.x/testing/"))

    return render_template('index.html', form=form)


