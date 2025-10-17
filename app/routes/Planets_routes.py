from flask import Blueprint 
from app.models.Planets import planets

Planets_bp = Blueprint("Planets_bp", __name__, url_prefix="/planets")

@Planets_bp.get("")
def get_all_Planets():
    Planet_response = []
    for Planet in planets:
        Planet_response.append({
            "id" : Planet.id , 
            "name":Planet.name,
            "description" : Planet.description , 
            "atmosphere":Planet.atmosphere
        })

    return Planet_response


