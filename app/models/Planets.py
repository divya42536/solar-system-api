from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Planets(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]        
    description: Mapped[str]
    atmosphere: Mapped[str]

    def to_dict(self):
        return {
        "id": self.id,
        "name": self.name,
        "description": self.description,
        "atmosphere" : self.atmosphere
    }

    @classmethod
    def from_dict(cls, planet_data):
        return cls(
            name=planet_data["name"],
            description= planet_data["description"],
            atmosphere= planet_data["atmosphere"]
            )