from model.BaseModel import BaseModel
from db import db


class Place(BaseModel):
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(1024), nullable=True)
    address = db.Column(db.String(128), nullable=False)
    city_id = db.Column(db.String(60), db.ForeignKey(
        'city.id'), nullable=False)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    host_id = db.Column(db.String(60), db.ForeignKey(
        'user.id'), nullable=False)
    number_of_rooms = db.Column(db.Integer, default=0)
    number_of_bathrooms = db.Column(db.Integer, default=0)
    max_guests = db.Column(db.Integer, default=0)
    price_per_night = db.Column(db.Integer, default=0)
    amenity_ids = []

    """  Place class that inherits from BaseModel. Represents a rental place with various attributes. """

    def __init__(self, name, description, address, city_id, latitude,
                 longitude, host_id, number_of_rooms, number_of_bathrooms, max_guests, price_per_night, amenity_ids=[], **kwargs):
        """ Initializes the Place with the given attributes. """
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self.address = address
        self.city_id = city_id
        self.latitude = latitude
        self.longitude = longitude
        self.host_id = host_id
        self.number_of_rooms = number_of_rooms
        self.number_of_bathrooms = number_of_bathrooms
        self.max_guests = max_guests
        self.amenity_ids = amenity_ids
        self.price_per_night = price_per_night

    def get_city_id(self):
        return self.city_id

    def __str__(self):
        return f"[Place] ({self.id}) {self.to_dict()}"

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'number_of_rooms': self.number_of_rooms,
            'number_of_bathrooms': self.number_of_bathrooms,
            'max_guests': self.max_guests,
            'price_by_night': self.price_per_night,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'city_id': self.city_id,
            'host_id': self.host_id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
