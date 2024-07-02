"""
  Now is easy to implement the database repository. The DBRepository
  should implement the Repository (Storage) interface and the methods defined
  in the abstract class Storage.

  The methods to implement are:
    - get_all
    - get
    - save
    - update
    - delete
    - reload (which can be empty)
"""

from src.models.base import Base
from src.persistence.repository import Repository
from src import db


class DBRepository(Repository):
    """Dummy DB repository"""

    def __init__(self) -> None:
        self.session = db.session

    def get_all(self, model_name: str) -> list:
        model_class = self._get_model_class(model_name)
        if model_class:
            return self.session.query(model_class).all()
        return []

    def get(self, model_name: str, obj_id: str) -> Base | None:
        model_class = self._get_model_class(model_name)
        return self.session.query(model_class).get(obj_id)

    def reload(self) -> None:
        pass

    def save(self, obj: Base) -> None:
        db.session.add(obj)
        db.session.commit()

    def update(self, obj: Base) -> Base | None:
        db.session.commit()

    def delete(self, obj: Base) -> bool:
        db.session.delete(obj)
        db.session.commit()
        return True
