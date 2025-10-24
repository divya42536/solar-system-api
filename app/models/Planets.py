from sqlalchemy.orm import Mapped, mapped_column
from ..db import db



class Planets(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]        
    description: Mapped[str]
    atmosphere: Mapped[str]
