import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
connection = psycopg2.connect('dbname=fyyur')

# TODO IMPLEMENT DATABASE URL
migrate = Migrate(app,db)
SQLALCHEMY_DATABASE_URI = 'postgresql://deemanasser@localhost:5432/fyyur'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://deemanasser@localhost:5432/fyyur'
connection = psycopg2.connect('dbname=fyyur')