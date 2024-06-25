from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db'
db = SQLAlchemy(app)

# Assurez-vous d'importer les modèles après l'initialisation de db
from src.models.user import User
from src.models.city import City
from src.models.country import Country
from src.models.place import Place
from src.models.review import Review

# Créez toutes les tables
with app.app_context():
    db.create_all()
