from server.models import Guest
from server.app import Resource
from flask import make_response


class Guests(Resource):
    def get(self):
        guests = Guest.query.all()
        if len(guests)> 0:
            return make_response([guest.to_dict() for guest in guests], 200)
        
        return make_response({'error': 'Episodes not found'}, 404)
