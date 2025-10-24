from flask import Blueprint , abort , make_response , request
from app.models.Planets import Planets 
from ..db import db

Planets_bp = Blueprint("Planets_bp", __name__, url_prefix="/planets")


@Planets_bp.post("")
def create_planet():
    request_body = request.get_json()
    name = request_body["name"]
    description = request_body["description"]
    atmosphere = request_body["atmosphere"]

    new_planet = Planets(name=name, description=description, atmosphere = atmosphere)
    db.session.add(new_planet)
    db.session.commit()

    response = {
        "id": new_planet.id,
        "name": new_planet.name,
        "description": new_planet.description,
        "atmosphere" : new_planet.atmosphere
    }
    return response, 201



@Planets_bp.get("")
def get_all_planets():
    query = db.select(Planets).order_by(Planets.id)
    planets = db.session.scalars(query)

    Planets_response = []
    for Planet in planets:
        Planets_response.append(
                {
                    "id": Planet.id,
                    "name": Planet.name,
                    "description": Planet.description,
                    "atmosphere": Planet.atmosphere
                }
            )
    return Planets_response


# # def validate_planet(id):
# #     try:
# #         id = int(id)
# #     except:
# #         response = {"message": f"planet {id} invalid"}
# #         abort(make_response(response, 400))

# #     for planet in planets:
# #         if planet.id == id:
# #             return planet

# #     response = {"message": f"planet {id} not found"}
# #     abort(make_response(response, 404))

# # @Planets_bp.get("")
# # def get_all_Planets():
    
# #     Planet_response = []
# #     for Planet in planets:
# #         Planet_response.append({
# #             "id" : Planet.id , 
# #             "name":Planet.name,
# #             "description" : Planet.description , 
# #             "atmosphere":Planet.atmosphere
# #         })

# #     return Planet_response
# # @Planets_bp.get("/<id>")
# # def get_one_Planet(id):
# #     planet = validate_planet(id)
# #     return {
# #             "id" : planet.id , 
# #             "name":planet.name,
# #             "description" : planet.description , 
# #             "atmosphere":planet.atmosphere
# #             }

