""" Entry point for the application. """

from flask.cli import FlaskGroup
from src import db
from src.models.user import User
from src.models.city import City
from src import create_app

cli = FlaskGroup(create_app=create_app)
@cli.command('create_db')
def create_db():
    db.drop_all()
    db.create_all()
    print("Database tables created")


if __name__ == "__main__":
    cli()
