# Ashley Towne
# 3/18/2016
# cherrypy 

import cherrypy
from moviecont import MovieController
from resetcont import ResetController
from usercont import UserController
from reccont import RecsController
from ratingscont import RatingsController
from _movie_database import _movie_database as mdb

datadir = '/afs/nd.edu/user37/cmc/Public/cse332_sp16/cherrypy/data'

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
                 '/'     : {'request.dispatch': dispatcher,}}
    
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
        reccon = RecsController()
        # GET
        dispatcher.connect('recs_get','/recommendations/:key', controller=reccon, action='GET', conditions=dict(method=['GET']))
        # PUT
        dispatcher.connect('recs_put','/recommendations/:key', controller=reccon, action='PUT', conditions=dict(method=['PUT']))
        # DELETE
        dispatcher.connect('recs_delete','/recommendations/', controller=reccon, action='DELETE', conditions=dict(method=['DELETE']))

        ##### RATINGS #####
        ratcon = RatingsController()
        # GET
        dispatcher.connect('ratings_get','/ratings/:key', controller=ratcon, action='GET', conditions=dict(method=['GET']))

        ##### RESET #####
        resetcon = ResetController(self.mdb)
        # POST/PUT
        dispatcher.connect('reset_put_all','/reset/', controller=resetcon, action='PUT_ALL', conditions=dict(method=['PUT']))
        dispatcher.connect('reset_put','/reset/:key', controller=resetcon, action='PUT', conditions=dict(method=['PUT']))

        self.load_posters(datadir+'/images.dat')
        print self.get_poster_by_mid(1)
        cherrypy.quickstart(app)
    
    def get_poster_by_mid(self, mid):
        if str(mid) in self.posters:
            return self.posters[str(mid)]
        else:
            return '/default.jpg'
    
    def load_posters(self,movie_file):
        self.posters = {}
        with open(movie_file) as f:
            for line in f:
                line = line.rstrip().split("::")
                self.posters[str(line[0])] = str(line[2])
    
if __name__ == '__main__':
    m = MovieService()
    m.start_service()
