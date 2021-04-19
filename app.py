# app.py

from flask import Flask
#from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///healthcare.db'
app.secret_key = "flask rocks!"

db = SQLAlchemy(app)