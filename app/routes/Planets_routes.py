from flask import Blueprint , abort , make_response
from app.models.Planets import planets

Planets_bp = Blueprint("Planets_bp", __name__, url_prefix="/planets")

def validate_planet(id):
    try:
        id = int(id)
    except:
        response = {"message": f"planet {id} invalid"}
        abort(make_response(response, 400))

    for planet in planets:
        if planet.id == id:
            return planet

    response = {"message": f"planet {id} not found"}
    abort(make_response(response, 404))

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
@Planets_bp.get("/<id>")
def get_one_Planet(id):
    planet = validate_planet(id)
    return {
            "id" : planet.id , 
            "name":planet.name,
            "description" : planet.description , 
            "atmosphere":planet.atmosphere
            }

