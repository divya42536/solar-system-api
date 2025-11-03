from flask import Blueprint , abort , make_response , request, Response
from app.models.Planets import Planets 
from ..db import db
from app.routes.routes_utilities import validate_model

bp = Blueprint("Planets_bp", __name__, url_prefix="/planets")


@bp.post("")
def create_planet():
    request_body = request.get_json()

    new_planet = Planets.from_dict(request_body)
    db.session.add(new_planet)
    db.session.commit()

    # response = {
    #     "id": new_planet.id,
    #     "name": new_planet.name,
    #     "description": new_planet.description,
    #     "atmosphere" : new_planet.atmosphere
    # }
    return new_planet.to_dict(), 201


@bp.get("")
def get_all_planets():
    query = db.select(Planets)
    
    name_param = request.args.get("name")
    if name_param:
        # find exact match for name
        query = query.where(Planets.name == name_param)
    
    atmosphere_param = request.args.get("atmosphere")
    if atmosphere_param:
        query = query.where(Planets.atmosphere.ilike(f"%{atmosphere_param}%"))

    description_param = request.args.get("description")
    if description_param:
        query = query.where(Planets.description.ilike(f"%{description_param}%"))
    query = query.order_by(Planets.id)
    planets = db.session.scalars(query)

    Planets_response = []
    for Planet in planets:
        Planets_response.append(
                Planet.to_dict()
            )
    return Planets_response

def validate_planet(id):
    try:
        id = int(id)
    except:
        response = {"message": f"planet {id} invalid"}
        abort(make_response(response, 400))

    query = db.select(Planets).where(Planets.id == id)
    planet = db.session.scalar(query)

    if not planet:
        response = {"message": f"planet {id} not found"}
        abort(make_response(response, 404))
    # for planet in Planets:
    #     if planet.id == id:
    return planet

    # response = {"message": f"planet {id} not found"}
    # abort(make_response(response, 404))
    
@bp.get("/<id>")
def get_one_planet(id):
    planet = validate_model(Planets, id)

    return planet.to_dict()
    #    { "id": planet.id,
    #     "name": planet.name,
    #     "description": planet.description,
    #     "atmosphere": planet.atmosphere
    # }

@bp.put("/<id>")
def replace_planet(id):
    planet = validate_model(Planets, id)

    request_body = request.get_json()
    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.atmosphere = request_body["atmosphere"]

    db.session.commit()
    return Response(status = 204 , mimetype = "application/json")

@bp.delete("/<id>")
def delete_planet(id):
    planet = validate_model(Planets, id)

    db.session.delete(planet)
    db.session.commit()

    return Response(status = 204 , mimetype = "application/json")