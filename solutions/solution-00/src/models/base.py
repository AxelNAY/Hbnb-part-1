from datetime import datetime
from typing import Optional
import uuid
from abc import ABC, abstractmethod
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import Column, String, DateTime, func
from src import db

class BaseMixin(ABC):
    """
    Base Interface for all models
    """

    @abstractmethod
    def to_dict(self) -> dict:
        """Returns the dictionary representation of the object"""

    @staticmethod
    @abstractmethod
    def create(data: dict) -> 'BaseMixin':
        """Creates a new object of the class"""

    @staticmethod
    @abstractmethod
    def update(entity_id: str, data: dict) -> 'BaseMixin' or None:
        """Updates an object of the class"""


class Base:
    """
    Base class for common model functionality
    """

    id = Column(String(36), primary_key=True, unique=True, nullable=False)
    created_at = Column(DateTime, default=func.current_timestamp())
    updated_at = Column(DateTime, onupdate=func.current_timestamp())

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    def __init__(
        self,
        id: Optional[str] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
        **kwargs,
    ) -> None:
        """
        Base class constructor
        If kwargs are provided, set them as attributes
        """
        super().__init__(**kwargs)
        self.id = str(id or uuid.uuid4())
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

    @classmethod
    def get(cls, id) -> 'Base' or None:
        """
        This is a common method to get a specific object
        of a class by its id

        If a class needs a different implementation,
        it should override this method
        """
        from src.persistence import repo

        return repo.get(cls.__name__.lower(), id)

    @classmethod
    def get_all(cls) -> list['Base']:
        """
        This is a common method to get all objects of a class

        If a class needs a different implementation,
        it should override this method
        """
        from src.persistence import repo

        return repo.get_all(cls.__name__.lower())

    @classmethod
    def delete(cls, id) -> bool:
        """
        This is a common method to delete a specific
        object of a class by its id

        If a class needs a different implementation,
        it should override this method
        """
        from src.persistence import repo

        obj = cls.get(id)

        if not obj:
            return False

        return repo.delete(obj)
