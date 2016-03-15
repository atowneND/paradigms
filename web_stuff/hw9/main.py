# Ashley Towne
# 3/18/2016
# cherrypy 

import cherrypy
from dcont import MovieController
from dcont import ResetController
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
        #conf = { 'global': {'server.socket_host': 'student02.cse.nd.edu', 'server.socket_port': 40092,},
        #         '/'     : {'request.dispatch': dispatcher,}}
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

        ##### RESET #####
        resetcon = ResetController(self.mdb)
        # POST/PUT
        dispatcher.connect('reset_put_all','/reset/', controller=resetcon, action='PUT', conditions=dict(method=['PUT_ALL']))
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
