# Import necessary libraries
import warnings
from datetime import timedelta
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Ignore specific warnings to prevent clutter in the console output
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Create a Flask application instance
app = Flask(__name__)

# Set a secret key for the application (used for session management, you should use a more secure key in production)
app.secret_key = 'qazwsxedcrfvtgbyhnujmiklop123456'

# Configure the application
app.config['SQLALCHEMY_ECHO'] = True  # Enable echoing SQL statements to the console
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)  # Set session lifetime to 30 minutes
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/flaskdb'  # Database URI
app.config['SQLALCHEMY_MAX_OVERFLOW'] = 0  # Prevent exceeding the maximum number of connections

# Create a SQLAlchemy database instance
db = SQLAlchemy(app)

# Create a Migrate instance for handling database migrations
migrate = Migrate(app, db)
