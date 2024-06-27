"""
Country related functionality
"""

from app import db

class Country(db.Model):
    """
    Country representation

    This class does NOT inherit from Base, you can't delete or update a country

    This class is used to get and list countries
    """

    __tablename__ = 'countries'
    
    code = db.Column(db.String(3), primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __init__(self, name: str, code: str, **kw) -> None:
        """Initialize a country"""
        super().__init__(**kw)
        self.name = name
        self.code = code

    def __repr__(self) -> str:
        """String representation"""
        return f"<Country {self.code} ({self.name})>"

    def to_dict(self) -> dict:
        """Returns the dictionary representation of the country"""
        return {
            "name": self.name,
            "code": self.code,
        }

    @staticmethod
    def get_all() -> list["Country"]:
        """Get all countries"""
        return Country.query.all()

    @staticmethod
    def get(code: str) -> "Country | None":
        """Get a country by its code"""
        return Country.query.get(code)

    @staticmethod
    def create(name: str, code: str) -> "Country":
        """Create a new country"""
        new_country = Country(name=name, code=code)
        db.session.add(new_country)
        db.session.commit()
        return new_country
