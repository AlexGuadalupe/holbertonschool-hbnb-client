from flask import Blueprint, request, jsonify, abort
from model.amenity import Amenity
from persistence.DataManager import DataManager
from db import db

amenity_blueprint = Blueprint('amenity_blueprint', __name__)
data_manager = DataManager()


# POST a new amenity
@amenity_blueprint.route('/amenities', methods=['POST'])
def create_amenity():
    if not request.json or 'name' not in request.json:
        abort(400, description="Missing required fields")

    name = request.json['name']

    existing_amenity = Amenity.query.filter_by(name=name).first()
    if existing_amenity:
        abort(409, description="Amenity name already exists")

    amenity = Amenity(name=name)
    db.session.add(amenity)
    db.session.commit()

    return jsonify(amenity.to_dict()), 201

# GET all amenities


@amenity_blueprint.route('/amenities', methods=['GET'])
def get_amenities():
    amenities = Amenity.query.all()
    return jsonify([amenity.to_dict() for amenity in amenities]), 200

# GET a specific amenity by amenity_id


@amenity_blueprint.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    amenity = Amenity.query.get(amenity_id)
    if not amenity:
        abort(404, description="Amenity not found")
    return jsonify(amenity.to_dict()), 200

# PUT update a specific amenity by amenity_id


@amenity_blueprint.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    amenity = Amenity.query.get(amenity_id)
    if not amenity:
        abort(404, description="Amenity not found")

    if not request.json:
        abort(400, description="Missing required fields")

    name = request.json.get('name', amenity.name)

    existing_amenity = Amenity.query.filter(
        Amenity.name == name, Amenity.id != amenity_id).first()
    if existing_amenity:
        abort(409, description="Amenity name already exists")

    amenity.name = name
    db.session.commit()

    return jsonify(amenity.to_dict()), 200

# DELETE a specific amenity by amenity_id


@amenity_blueprint.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    amenity = Amenity.query.get(amenity_id)
    if not amenity:
        abort(404, description="Amenity not found")

    db.session.delete(amenity)
    db.session.commit()

    return '', 204
