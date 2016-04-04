# Ashley Towne
# 3/18/2016
# cherrypy

import cherrypy
from controllers.moviecont import MovieController
from controllers.resetcont import ResetController
from controllers.usercont import UserController
from controllers.reccont import RecsController
from controllers.ratingscont import RatingsController
from _movie_database import _movie_database as mdb

def CORS():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = ""
    cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, PUT, POST, DELETE, OPTIONS"
    cherrypy.response.headers["Access-Control-Allow-Credentials"] = "true"

class MovieService:
    def __init__(self):
        self.posters = {}
        self.mdb = mdb()
        self.mdb.load_movies('ml-1m/movies.dat')
        self.mdb.load_users('ml-1m/users.dat')
        self.mdb.load_ratings('ml-1m/ratings.dat')

    def start_service(self):
        dispatcher = cherrypy.dispatch.RoutesDispatcher()
        conf = { 'global': {'server.socket_host': '127.0.0.1', 'server.socket_port': 40092,},
                '/'     : {'request.dispatch': dispatcher,'tools.CORS.on':True,}}

        cherrypy.config.update(conf)
        app = cherrypy.tree.mount(None, config=conf)

        ##### MOVIE #####
        moviecon = MovieController(self.mdb)
        # GET
        dispatcher.connect('movie_get_all','/movies/', controller=moviecon, action='GET_ALL', conditions=dict(method=['GET']))
        dispatcher.connect('movie_get','/movies/:key', controller=moviecon, action='GET', conditions=dict(method=['GET']))
        # POST/PUT
        dispatcher.connect('movie_post','/movies/', controller=moviecon, action='POST', conditions=dict(method=['POST']))
        dispatcher.connect('movie_put','/movies/:key', controller=moviecon, action='PUT', conditions=dict(method=['PUT']))
        # DELETE
        dispatcher.connect('movie_delete_all','/movies/', controller=moviecon, action='DELETE_ALL', conditions=dict(method=['DELETE']))
        dispatcher.connect('movie_delete','/movies/:key', controller=moviecon, action='DELETE', conditions=dict(method=['DELETE']))

        ##### USERS #####
        usercon = UserController(self.mdb)
        # GET
        dispatcher.connect('user_get_all','/users/', controller=usercon, action='GET_ALL', conditions=dict(method=['GET']))
        dispatcher.connect('user_get','/users/:key', controller=usercon, action='GET', conditions=dict(method=['GET']))
        # POST/PUT
        dispatcher.connect('user_post','/users/', controller=usercon, action='POST', conditions=dict(method=['POST']))
        dispatcher.connect('user_put','/users/:key', controller=usercon, action='PUT', conditions=dict(method=['PUT']))
        # DELETE
        dispatcher.connect('user_delete_all','/users/', controller=usercon, action='DELETE_ALL', conditions=dict(method=['DELETE']))
        dispatcher.connect('user_delete','/users/:key', controller=usercon, action='DELETE', conditions=dict(method=['DELETE']))

        ##### REC'S #####
        reccon = RecsController(self.mdb)
        # GET
        dispatcher.connect('recs_get','/recommendations/:key', controller=reccon, action='GET', conditions=dict(method=['GET']))
        # PUT
        dispatcher.connect('recs_put','/recommendations/:key', controller=reccon, action='PUT', conditions=dict(method=['PUT']))
        # DELETE
        dispatcher.connect('recs_delete','/recommendations/', controller=reccon, action='DELETE', conditions=dict(method=['DELETE']))

        ##### RATINGS #####
        ratcon = RatingsController(self.mdb)
        # GET
        dispatcher.connect('ratings_get','/ratings/:key', controller=ratcon, action='GET', conditions=dict(method=['GET']))

        ##### RESET #####
        resetcon = ResetController(self.mdb)
        # POST/PUT
        dispatcher.connect('reset_put_all','/reset/', controller=resetcon, action='PUT_ALL', conditions=dict(method=['PUT']))
        dispatcher.connect('reset_put','/reset/:key', controller=resetcon, action='PUT', conditions=dict(method=['PUT']))

        cherrypy.quickstart(app)

if __name__ == '__main__':
    cherrypy.tools.CORS = cherrypy.Tool('before_finalize',CORS)
    m = MovieService()
    m.start_service()
