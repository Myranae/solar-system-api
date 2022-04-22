from flask import Blueprint, jsonify


class Planet:
    def __init__(self, id, name, description, color):
        self.id = id
        self.name = name
        self.description = description
        self.color = color 

planets = [
    Planet(1, "Mercury", "Super small, comparatively", "slate gray"),
    Planet(2, "Venus", "It's sooo hot!", "yellow-white"),
    Planet(3, "Earth", "Home to humans", "blue-green"),
    Planet(4, "Mars", "The red one", "red"),
    Planet(5, "Jupiter", "The biggest of them all", "orange-yellow"),
    Planet(6, "Saturn", "What beautiful rings it has!", "hazy yellow-brown"),
    Planet(7, "Uranus", "Tilted sideways", "blue-green"),
    Planet(8, "Neptune", "Giant, stormy, blue", "blue"),
    Planet(9, "Maybe Pluto", "Is it really a planet??", "reddish-brown")
    ]

bp = Blueprint("planets", __name__, url_prefix="/planets")

@bp.route("", methods=["GET"])
def get_planets():
    results_list = []
    for planet in planets:
        results_list.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "color": planet.color,
            }
            )
    return jsonify(results_list)
