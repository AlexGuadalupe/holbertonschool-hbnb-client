from flask import Blueprint, request, jsonify, abort
from model.place import Place
from persistence.DataManager import DataManager
from db import db


place_blueprint = Blueprint('place_blueprint', __name__)
data_manager = DataManager()


@place_blueprint.route('/places', methods=['POST'])
def create_place():
    if not request.json:
        abort(400, description="Missing required fields")

    data = request.json
    place = Place(
        name=data.get('name'),
        description=data.get('description'),
        address=data.get('address'),
        city_id=data.get('city_id'),
        latitude=data.get('latitude'),
        longitude=data.get('longitude'),
        host_id=data.get('host_id'),
        number_of_rooms=data.get('number_of_rooms'),
        number_of_bathrooms=data.get('number_of_bathrooms'),
        price_per_night=data.get('price_per_night'),
        max_guests=data.get('max_guests'),
        amenity_ids=data.get('amenity_ids')
    )

    db.session.add(place)
    db.session.commit()
    return jsonify(place.to_dict()), 201


@place_blueprint.route('/places', methods=['GET'])
def get_places():
    places = Place.query.all()
    return jsonify([place.to_dict() for place in places]), 200


@place_blueprint.route('/places/<place_id>', methods=['GET'])
def get_place(place_id):
    place = Place.query.get(place_id)
    if not place:
        abort(404, description="Place not found")
    return jsonify(place.to_dict()), 200


@place_blueprint.route('/places/<place_id>', methods=['PUT'])
def update_place(place_id):
    place = Place.query.get(place_id)
    if not place:
        abort(404, description="Place not found")

    if not request.json:
        abort(400, description="Missing required fields")

    data = request.json
    place.name = data.get('name', place.name)
    place.description = data.get('description', place.description)
    place.address = data.get('address', place.address)
    place.city_id = data.get('city_id', place.city_id)
    place.latitude = data.get('latitude', place.latitude)
    place.longitude = data.get('longitude', place.longitude)
    place.host_id = data.get('host_id', place.host_id)
    place.number_of_rooms = data.get('number_of_rooms', place.number_of_rooms)
    place.number_of_bathrooms = data.get(
        'number_of_bathrooms', place.number_of_bathrooms)
    place.price_per_night = data.get('price_per_night', place.price_per_night)
    place.max_guests = data.get('max_guests', place.max_guests)
    place.amenity_ids = data.get('amenity_ids', place.amenity_ids)

    db.session.commit()
    return jsonify(place.to_dict()), 200


@place_blueprint.route('/places/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    place = Place.query.get(place_id)
    if not place:
        abort(404, description="Place not found")
    db.session.delete(place)
    db.session.commit()
    return '', 204
