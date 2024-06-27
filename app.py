from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db'
db = SQLAlchemy(app)


from models.user import User
from models.city import City
from models.country import Country
from models.place import Place
from models.review import Review

with app.app_context():
    db.create_all()
