from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
from model import register, login
from modeldatabase import Userdata, Session, engine
import os

app = Flask(__name__)

session = Session()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Signup', methods=['GET', 'POST'])
def Signup():
    form = register()
    if form.validate_on_submit():
        user = Userdata(username=form.username.data, email=form.email.data, password=form.password.data)
        session.add(user)
        session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('Login'))
    return render_template('Signup.html', title='Signup', form=form)

"""
@app.route('/Login', methods=['GET', 'POST'])
def Login():
    form = login()
    if form.validate_on_submit():
"""