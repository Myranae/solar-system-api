from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.moon import Moon

bp = Blueprint("moons", __name__, url_prefix="/moons")

@bp.route("", methods=["GET"])
def read_all_moons():
    name_param = request.args.get("name")
    description_param = request.args.get("description")
    size_param = request.args.get("size")

    moons = Moon.query

    if name_param:
        moons = moons.filter_by(name=name_param)
    if description_param:
        moons = moons.filter_by(description=description_param)
    if size_param:
        moons = moons.filter_by(size=size_param)
    
    moons = moons.all()

    moons_response = []
    for moon in moons:
        moons_response.append(
            {
                "id": moon.id,
                "name": moon.name,
                "description": moon.description,
                "size": moon.size
            }
        )
    return jsonify(moons_response)