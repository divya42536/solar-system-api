from flask import Blueprint, abort, make_response, request, Response
from ..db import db
from app.models.Moons import Moons
from app.models.Planets import Planets
from .routes_utilities import validate_model, create_model, get_models_with_filters

bp = Blueprint("Moons_bp", __name__, url_prefix="/Moons")

@bp.post("")
def create_moon():
    request_body = request.get_json()
    return create_model(Moons, request_body)

@bp.get("")
def get_all_moons():
    return get_models_with_filters(Moons, request.args)

@bp.post("/<moon_id>/planets")
def create_planet_with_moon(moon_id):
    moon = validate_model(Moons, moon_id)
    
    request_body = request.get_json()
    request_body["moon_id"] = moon.id

    return create_model(Planets, request_body)

@bp.get("/<moon_id>/planets")
def get_books_by_moon(moon_id):
    moon = validate_model(Moons, moon_id)
    response = [Moons.to_dict() for Moons in moon.planets]
    return response