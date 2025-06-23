from server.models import User
from server.app import Resource, db
from flask_jwt_extended import create_access_token
from flask import request, make_response, jsonify

class Login(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(username=data.get('username')).first()
        if user:
            if user.authenticate(data.get('password')):
                at = create_access_token(identity=user.id)
                return make_response(jsonify(access_token=at), 200)
        return make_response({'error': 'Incorrect username or password'}, 400)


class Register(Resource):
    def post(self):
        data = request.get_json()
        try:
            user = User(username=data.get('username'))

            user.password_hash = data.get('password')
            db.session.add(user)
            db.session.commit()

            return make_response(user.to_dict(), 201)
        except ValueError as err:
            return make_response({'error': f'{err}'})
        except AttributeError as er:
            return make_response({'error': f'{er}'})
    


        
