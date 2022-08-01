from flask import render_template

from app import app


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
    return render_template('index.html', title='Blog', user=user, posts=posts)
