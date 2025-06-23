from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api, Resource
from dotenv import load_dotenv
from flask_bcrypt import Bcrypt
from server.models import Episode, Appearance, Guest, User
from server.config import db
from server.controllers import addResource

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

load_dotenv()

app = Flask(__name__)

app.config.from_prefixed_env(prefix='FLASK')

db.init_app(app=app)
migrate = Migrate(app=app, db=db)
api = Api(app=app)
jwt = JWTManager(app=app)
bcrypt = Bcrypt(app)

addResource()
