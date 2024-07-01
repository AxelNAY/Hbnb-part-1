from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.config import get_config
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db'
db = SQLAlchemy(app)

from src.models.user import User
from src.models.city import City
from src.models.country import Country
from src.models.place import Place
from src.models.review import Review


with app.app_context():
    db.create_all()
