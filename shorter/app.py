from flask import render_template

from shorter import app
from shorter.forms import URLForm


@app.route('/', methods=['get', 'post'])
def index():
    form = URLForm()
    if form.validate_on_submit():
        print(form.url.data)

    return render_template('index.html', form=form)


