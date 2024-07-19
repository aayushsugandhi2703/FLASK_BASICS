from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
from model import register, login
from modeldatabase import Userdata, Session, engine
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
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
    login_user(user)
        flash(f'Login successful!', 'success')
        return redirect(url_for('index'))
    return render_template('Login.html', title='Login', form=form)
"""
@app.route('/Logout')
@login_required
def logout():
    logout_user()
    flash(f'Logout successful!', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
