from server.models import Appearance
from server.app import Resource, db
from flask_jwt_extended import jwt_required
from flask import request, make_response

class Appearances(Resource):
    @jwt_required()
    def post(self):
        data = request.get_json()
        appearance = Appearance(rating=data.get('rating'))
        try:
            for attr in data:
                setattr(appearance, attr, data[attr])
            
            db.session.add(appearance)
            db.session.commit()

            return make_response(appearance.to_dict(), 201)
        except ValueError as err:
            return make_response({'error': f'{err}'})
        
   
