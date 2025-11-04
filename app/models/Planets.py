from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from ..db import db
from typing import Optional
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from .Moons import Moons


class Planets(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]        
    description: Mapped[str]
    atmosphere: Mapped[str]
    moon_id: Mapped[Optional[int]] = mapped_column(ForeignKey("moons.id"))
    moon: Mapped[Optional["Moons"]] = relationship(back_populates="planets")

    def to_dict(self):
       
        Planets_as_dict = {}
        Planets_as_dict["id"] = self.id
        Planets_as_dict["name"] = self.name
        Planets_as_dict["description"] = self.description
        Planets_as_dict["atmosphere"] = self.atmosphere

        if self.moon:
            Planets_as_dict["moon"] = self.moon.name


        return Planets_as_dict

    @classmethod
    def from_dict(cls, planet_data):
        moon_id = planet_data.get("moon_id")

        return cls(
            name=planet_data["name"],
            description= planet_data["description"],
            atmosphere= planet_data["atmosphere"],
            moon_id=moon_id
            )