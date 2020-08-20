from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import URL


class URLForm(FlaskForm):
    url = StringField("URL: ", validators=(URL(),))
