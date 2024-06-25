from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['USE_DATABASE'] = os.getenv('USE_DATABASE', 'False').lower() in ['true', '1']

db = SQLAlchemy(app)

# Importer les routes et les controllers
import controllers
import routes

if __name__ == '__main__':
    app.run(debug=True)
