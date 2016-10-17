# Imports always come first
import hashlib
from flask import Flask, request, render_template, abort, redirect, url_for


# Our first task is to create an instance
# of the Flask class. This is the core of
# our web application.
app = Flask('chirpy')

# By convention, all config entries are uppercase
DEBUG = True
PORT = 8686
SECRET_KEY = 'suchsecretwow'

# Tell our Flask instance to use the above settings
app.config.from_object(__name__)



# Our very wonderful database
chirpy_posts_db = []

# We create our first 'route'
# This tells our Flask instance that anyone connecting to
# http://chirpy/ will get this reponse
@app.route('/')
def index():
    return render_template('chirpy.html', posts=chirpy_posts_db)


# A second route, this time for submitting
# new posts. Note that we only allow http
# 'POST' methods.
@app.route('/submit', methods=['POST'])
def submit_post():
    post = {}
    post['email'] = request.form.get('email').lower().strip()
    post['post'] = request.form.get('post')
    post['avatar'] = 'https://www.gravatar.com/avatar/{}.json'.format(hashlib.md5(post['email'].encode('utf-8')).hexdigest())
    chirpy_posts_db.append(post)
    return redirect(url_for('index'))
