from flask import abort, make_response
from ..db import db

def validate_model(cls,id):
    try:
        id = int(id)
    except:
        response = {"message": f"{cls.__name__} {id} invalid"}
        abort(make_response(response, 400))

    query = db.select(cls).where(cls.id == id)
    model = db.session.scalar(query)

    if not model:
        response = {"message": f"{cls.__name__} planet {id} not found"}
        abort(make_response(response, 404))
    # for planet in Planets:
    #     if planet.id == id:
    return model

    # response = {"message": f"planet {id} not found"}
    # abort(make_response(response, 404))