from server.models import Episode
from server.app import Resource, db
from flask_jwt_extended import jwt_required
from flask import make_response


class Episodes(Resource):
    def get(self):
        episodes = Episode.query.all()
        if len(episodes)> 0:
            return make_response([episode.to_dict() for episode in episodes], 200)
        
        return make_response({'error': 'Episodes not found'}, 404)

class EpisodeById(Resource):
    def get(self, id):
        episode = Episode.query.filter_by(id=id).first()
        if episode:
            return make_response(episode.to_dict(), 200)
        
        return make_response({'error': 'Episode not found'}, 404)
        
    @jwt_required()
    def delete(self, id):
        episode = Episode.query.filter_by(id=id).first()

        if episode:
            db.session.delete(episode)
            db.session.commit()

            return make_response({}, 204)
        return make_response({'error': 'Episode not found'}, 404)