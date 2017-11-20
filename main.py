
#!/usr/bin/python
import json
import requests
from flask import Flask, render_template, url_for, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy
import os
from scifi_finder import API_KEY

app = Flask(__name__)
app.secret_key = "a key no one will ever guess"

# SQLAlchemy object
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)

# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80))

# class Form?

# Views
@app.route('/')
@app.route('/index')
def main():
    r = requests.get('https://api.themoviedb.org/3/movie/now_playing?api_key=9c992a0026819239213f139fa35c40dc&language=en-US&page=1')
    now_playing = r.json()
    movie_list = []
    return render_template('index.html', now_playing=now_playing)



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        user = User(email=email)

        db.session.add(user)
        db.session.commit()
        flash("Thank you for signing up! You will receive your first very own SciFi Galore soon!")
        return redirect(url_for('main'))

    return render_template('signup.html')



if __name__== '__main__':
    app.run(debug=True)






# To-Do Breakdown:

# Flask-mail to newsletter
# Notify via email (weekly)
# make a subscription service web app
    # working db
    # no new page but JS for /signup?
    # Add WTFforms instead?
    # working form to db
# posters?
# implement unsubscribe
