from flask import Flask, render_template, redirect, url_for, flash
from model import register, logins 
from modeldatabase import Userdata, Session
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Create Flask app instance
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')

# Create a database session
session = Session()

login_manager = LoginManager(app)      # Initialize Flask-Login
login_manager.login_view = 'login'          # Set the login view (page to redirect to for unauthorized access)


# Define user loader function for Flask-Login (loads user by ID)
@login_manager.user_loader
def load_user(user_id):
    return session.query(Userdata).get(int(user_id))

# Route for the main page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new')
@login_required
def new():
    return render_template('new.html')

# Route for signup ('register' function creates a form)
@app.route('/Signup', methods=['GET', 'POST'])
def Signup():
    form = register()
    if form.validate_on_submit():
        # Check if email already exists
        existing_user = session.query(Userdata).filter_by(email=form.email.data).first()
        if existing_user:
            flash('Email address already in use. Please choose a different one.', 'danger')
            return render_template('signup.html', title='Signup', form=form)
        
        user = Userdata(username=form.username.data, email=form.email.data, password=form.password.data)
        session.add(user)
        session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))  # Redirect to login after signup
    return render_template('Signup.html', title='Signup', form=form)

# Route for login ( 'login' function creates a form)
@app.route('/Login', methods=['GET', 'POST'])  # Corrected route definition
def login():  # Function name should match the route definition
    form = logins()
    if form.validate_on_submit():
        user = session.query(Userdata).filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash(f'Login successful!', 'success')
            return redirect(url_for('new'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

# Route for logout with login required
@app.route('/Logout')
@login_required
def logout():
    logout_user()
    flash('Logout successful!', 'success')
    return redirect(url_for('login'))

# Route for admin panel with login required
@app.route('/admin')
@login_required
def admin():
    print(f'Current user: {current_user.username}')
    if current_user.email == 'aayush@gmail.com':
        return 'Welcome to the admin panel, ' + current_user.username
    return 'Access denied', 403

if __name__ == '__main__':
    app.run(debug=True)
