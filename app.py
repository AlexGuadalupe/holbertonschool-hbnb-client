from flask import Flask
from db import db
import os
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from flask_jwt_extended import create_access_token, create_refresh_token
from api.user_manager import user_manager_blueprint
from api.country_city_manager import country_city_manager_blueprint
from api.amenity_manager import amenity_blueprint
from api.place_manager import place_blueprint
from api.review_manager import review_blueprint
from flask import jsonify, request
from model.user import User

app = Flask(__name__)


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///development.db'
    JWT_SECRET_KEY = 'super-secret'


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


environment_config = DevelopmentConfig if os.environ.get(
    'ENV') == 'development' else ProductionConfig

app.config.from_object(environment_config)
app.config


db.init_app(app)
jwt = JWTManager(app)


@app.route('/')
def home():
    return 'Welcome to api'


@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


@app.route('/admin', methods=['GET'])
@jwt_required()
def admin():
    current_user = get_jwt_identity()
    user = User.query.filter_by(email=current_user).first()
    if user and user.is_admin:
        return jsonify(admin_access=True), 200
    return jsonify({"msg": "Admin privilege required"}), 403


@app.route('/token/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    new_token = create_access_token(identity=current_user)
    return jsonify({'access_token': new_token})

# Otros endpoints y configuración de la aplicación aquí


app.register_blueprint(user_manager_blueprint)
app.register_blueprint(country_city_manager_blueprint)
app.register_blueprint(amenity_blueprint)
app.register_blueprint(place_blueprint)
app.register_blueprint(review_blueprint)

with app.app_context():
    db.create_all()

print(f"USE_DATABASE: {os.getenv('USE_DATABASE')}")
if __name__ == "__main__":
    app.run(debug=True)
