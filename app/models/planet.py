from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    color = db.Column(db.String)
    moons = db.relationship("Moon", back_populates="planet")

    def to_dict(self):
        return {
            "planet_id": self.id,
            "name": self.name,
            "description": self.description,
            "color": self.color,
            "moons": self.moons
        }

    @classmethod
    def from_dict(cls, data_dict):
        return Planet(
            name=data_dict["name"]
        )