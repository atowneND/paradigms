# Ashley Towne
# 3/18/2016
# cherrypy 

import cherrypy
from dcont import DictionaryController

datadir = '/afs/nd.edu/user37/cmc/Public/cse332_sp16/cherrypy/data'

class MovieService:
    def __init__(self):
        self.posters = {}

    def start_service(self):
        dispatcher = cherrypy.dispatch.RoutesDispatcher()
        conf = { 'global': {'server.socket_host': '127.0.0.1', 'server.socket_port': 40092,},
                 '/'     : {'request.dispatch': dispatcher,}}
    
        cherrypy.config.update(conf)
        app = cherrypy.tree.mount(None, config=conf)
    
        dictcon = DictionaryController()
    
        # GET
        dispatcher.connect('dict_get_all','/dictionary/', controller=dictcon, action='GET_ALL', conditions=dict(method=['GET']))
        dispatcher.connect('dict_get','/dictionary/:key', controller=dictcon, action='GET', conditions=dict(method=['GET']))
    
        # POST/PUT
        dispatcher.connect('dict_post','/dictionary/', controller=dictcon, action='POST', conditions=dict(method=['POST']))
        dispatcher.connect('dict_put','/dictionary/:key', controller=dictcon, action='PUT', conditions=dict(method=['PUT']))
    
        # DELETE
        dispatcher.connect('dict_delete_all','/dictionary/', controller=dictcon, action='DELETE_ALL', conditions=dict(method=['DELETE']))
        dispatcher.connect('dict_delete','/dictionary/:key', controller=dictcon, action='DELETE', conditions=dict(method=['DELETE']))
    
        self.load_posters(datadir+'/images.dat')
        print self.get_poster_by_mid(1)
        exit()
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
