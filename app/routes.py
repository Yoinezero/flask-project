from flask import render_template, flash, redirect, url_for

from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Arseni'}
    posts = [
        {
            'author': {'username': 'Smith'},
            'body': 'Beautiful day today!'
        },
        {
            'author': {'username': 'Sushi'},
            'body': 'Special offer! 3 for the price of 2!'
        },
        {
            'author': {'username': 'Suzaki'},
            'body': 'Omae wa mou shindeiru!'
        },
    ]
    return render_template('index.jinja2', title='Blog', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.jinja2', title='Sign In', form=form)
