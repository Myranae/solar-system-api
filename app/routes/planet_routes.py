from flask import Blueprint, jsonify, abort, make_response, request
from app import db
from app.models.planet import Planet
from app.models.moon import Moon

bp = Blueprint("planets", __name__, url_prefix="/planets")

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except ValueError:
        abort(make_response(f"Planet {planet_id} is invalid", 400))

    planet = Planet.query.get(planet_id)

    if not planet:
        abort(make_response(f"Planet {planet_id} not found", 404))
    
    return planet


@bp.route("", methods=["POST"])
def create_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name = request_body["name"],
        description = request_body["description"],
        color = request_body["color"]
    )

    db.session.add(new_planet)
    db.session.commit()

    return make_response(jsonify(f"Planet {new_planet.name} successfully created"), 201)

@bp.route("", methods=["GET"])
def read_all_planets():
    name_param = request.args.get("name")
    description_param = request.args.get("description")
    color_param = request.args.get("color")

    planets = Planet.query

    if name_param:
        planets = planets.filter_by(name=name_param)
    if description_param:
        planets = planets.filter_by(description=description_param)
    if color_param:
        planets = planets.filter_by(color=color_param)
    
    planets = planets.all()

    #.query provides an in progress query

    planets_response = []
    for planet in planets:
        planets_response.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "color": planet.color
            }
        )
    return jsonify(planets_response)

@bp.route("/<planet_id>", methods=["GET"])
def read_one_planet(planet_id):
    planet = validate_planet(planet_id)
    
    return planet.to_dict()

@bp.route("/<planet_id>", methods=["DELETE"])
def delete_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()
    
    return jsonify(f'Planet {planet_id} successfully deleted')

@bp.route("/<planet_id>", methods=["PUT"])
def update_planet(planet_id):
    planet = validate_planet(planet_id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.color = request_body["color"]

    db.session.commit()

    return make_response(jsonify(f"Planet {planet_id} was successfully replaced."))

# NESTED ROUTES
@bp.route("/<planet_id>/moons", methods=["POST"])
def create_moon(planet_id):
    request_body = request.get_json()
    planet = validate_planet(planet_id)

    new_moon = Moon(
        name = request_body["name"],
        description = request_body["description"],
        size = request_body["size"],
        planet = planet
    )

    db.session.add(new_moon)
    db.session.commit()

    return make_response(jsonify(f"Moon {new_moon.name} successfully created"), 201)