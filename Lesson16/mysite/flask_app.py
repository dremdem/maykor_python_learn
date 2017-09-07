#-*- coding: utf-8 -*-
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, redirect, url_for

from forms import TestForm

app = Flask(__name__, template_folder='/home/dremdem/mysite/templates')
app.secret_key = 's3cr3t'

class NobodyCare(object):

    def __init__(self):
        self.just_a = 'AAAAAAAAAA'
        self.just_b = 'BBBBBBBBB'
        self.just_123 = '123'

        self.people = [u'Иванов', u'Петров', u'Сидоров']




@app.route('/test', methods=['GET', 'POST'])
def test():
    t1 = u'Еще не запускали!'
    form = TestForm()
    if form.validate_on_submit():
        t1 = form.test1.data
    return render_template('test.html', form=form, t1=t1)

@app.route('/')
def hello_world():
    return render_template('hello.html', a='100')

