from flask import render_template, request, redirect, url_for
from app import app

users = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user = {
            'name': request.form['name'],
            'age': request.form['age'],
            'city': request.form['city'],
            'hobby': request.form['hobby']
        }
        users.append(user)
        return redirect(url_for('index'))
    return render_template('index.html', users=users)