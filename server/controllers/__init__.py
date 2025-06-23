from server.controllers.auth_controller import Register, Login
from server.controllers.episode_controller import Episodes, EpisodeById
from server.controllers.guest_controller import Guests
from server.controllers.appearance_controller import Appearances


def addResource():
    from server.app import api
    api.add_resource(Register, '/register', endpoint='register')
    api.add_resource(Login, '/login', endpoint='login')
    api.add_resource(EpisodeById, '/episodes/<int:id>')
    api.add_resource(Episodes, '/episodes')
    api.add_resource(Guests, '/guests')
    api.add_resource(Appearances, '/appearances')