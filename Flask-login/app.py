from flask import Flask, render_template, redirect, url_for, flash
from model import register, logins  # Assuming these functions define forms
from modeldatabase import Userdata, Session
from flask_login import LoginManager, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Create Flask app instance
app = Flask(__name__)

# Configure database connection (replace with your actual connection string)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

# Suppress SQLAlchemy modification tracking warning
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Set a secret key for session management (replace with a strong random string)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')

# Create a database session
session = Session()

# Initialize Flask-Login
login_manager = LoginManager(app)

# Set the login view (page to redirect to for unauthorized access)
login_manager.login_view = 'login'

# Define user loader function for Flask-Login (loads user by ID)
@login_manager.user_loader
def load_user(user_id):
    return session.query(Userdata).get(int(user_id))

# Route for the main page (replace with your actual content)
@app.route('/')
def index():
    return render_template('index.html')

# Route for signup (assumes 'register' function creates a form)
@app.route('/Signup', methods=['GET', 'POST'])
def Signup():
    form = register()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        user = Userdata(username=form.username.data, email=form.email.data, password=hashed_password)
        session.add(user)
        session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('Signup'))  # Redirect to login after signup
    return render_template('Signup.html', title='Signup', form=form)

# Route for login (corrected typo, assumes 'login' function creates a form)
@app.route('/Login', methods=['GET', 'POST'])  # Corrected route definition
def login():  # Function name should match the route definition
    form = logins()
    if form.validate_on_submit():
        user = session.query(Userdata).filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash(f'Login successful!', 'success')
            return redirect(url_for('index'))
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

# Run the Flask app in debug mode (not recommended for production)
if __name__ == '__main__':
    app.run(debug=True)
