from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'name': 'Salman'}
    return render_template('index.html', username=user)


@app.route('/contact')
def contact():
    return "Contact"
