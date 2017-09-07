from flask_wtf import Form
from wtforms import StringField

class TestForm(Form):
    test1 = StringField('test1')
    test2 = StringField('test2')