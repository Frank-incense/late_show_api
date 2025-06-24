from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt
from server.models import Episode, Appearance, Guest, User
from server.config import db
from server.controllers import addResource

from flask_jwt_extended import JWTManager
from flask_jwt_extended.exceptions import NoAuthorizationError

load_dotenv()

app = Flask(__name__)

app.config.from_prefixed_env(prefix='FLASK')

db.init_app(app=app)
migrate = Migrate(app=app, db=db)
api = Api(app=app)
jwt = JWTManager(app=app)

@jwt.unauthorized_loader
def custom_unauthorized_response(err_msg):
    return jsonify({
        "error": "Authorization required",
        "message": err_msg
    }), 401
bcrypt = Bcrypt(app)

addResource()
