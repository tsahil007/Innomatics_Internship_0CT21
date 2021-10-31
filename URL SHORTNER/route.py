from flask import Flask, render_template, request, Blueprint, url_for
import random

from werkzeug.utils import redirect

views = Blueprint('views', __name__)
######################################
from .model import History
from . import db


@views.route('/')
def home_get():
    return render_template('index.html')


@views.route('/', methods=['POST'])
def home_post():
    url_user = request.form.get('in_1')
    url = History.query.filter_by(url_user=url_user).first()
    if url:
        return render_template('shortened.html', shorten_url=url.shorten_url)
    else:
        shorten_url = random.randint(1000, 9999)
        new_url = History(url_user=url_user, shorten_url=shorten_url)
        db.session.add(new_url)
        db.session.commit()
        return render_template('shortened.html', shorten_url=shorten_url)


@views.route('/history')
def history_get():
    result = db.session.query(History).all()
    return render_template('history.html', result=result)


@views.route('/user/<url>')
def fun(url):
    data_url = History.query.filter_by(shorten_url=url).first()
    if data_url:
        return redirect(data_url.url_user)
    return "Incorrect URL"
######################################
