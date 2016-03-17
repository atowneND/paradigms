# Ashley Towne
# Movie Controller

import json
import cherrypy

datadir = '/afs/nd.edu/user37/cmc/Public/cse332_sp16/cherrypy/data'

class MovieController():
    def __init__(self, mdb):
        self.mdb = mdb
        self.load_posters(datadir+'/images.dat')

    def GET(self, key):
        output = {'result':'success'}
        try:
            output['genres'] = self.mdb.movies[int(key)]['genres']
            output['title'] = self.mdb.movies[int(key)]['title']
            output['id'] = int(key)
            output['img'] = self.get_poster_by_mid(int(key))
        except KeyError as ex:
            output['result'] = 'error'
            output['message'] = 'key not found'
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = 'invalid input data'
        return json.dumps(output, encoding='latin-1')

    def GET_ALL(self):
        output = {'result':'success'}
        try:
            movielist = []
            for k in self.mdb.movies.keys():
                movielist.append(
                    # needs to be a dict, not a string
                    {'result':'success',
                    'genres':self.mdb.movies[int(k)]['genres'],
                    'title':self.mdb.movies[int(k)]['title'],
                    'id':int(str(k)),
                    'img':self.get_poster_by_mid(int(k))},
                )
            output['movies'] = movielist
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = ex
        return json.dumps(output, encoding='latin-1')

    def POST(self):
        output = {'result':'success'}
        try:
            instr = cherrypy.request.body.read()
            indict = json.loads(instr)
            new_id = max([int(k) for k in self.mdb.movies.keys()]) + 1
            self.mdb.set_movie(new_id, [indict['title'], indict['genres']])
            output['id'] = new_id
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = ex
        return json.dumps(output, encoding='latin-1')

    def PUT(self, key):
        output = {'result':'success'}
        try: 
            instr = cherrypy.request.body.read()
            indict = json.loads(instr)
            self.mdb.set_movie(int(key), [indict['title'],indict['genres']])
            output['id'] = int(key)
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = ex
        return json.dumps(output, encoding='latin-1')

    def DELETE(self, key):
        output = {'result':'success'}
        try:
            self.mdb.delete_movie(int(key))
            output['message'] = "success: key {i} deleted".format(i=key)
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = ex
        return json.dumps(output, encoding='latin-1')

    def DELETE_ALL(self):
        output = {'result':'success'}
        try: 
            self.mdb.movies = {}
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = ex
        return json.dumps(output, encoding='latin-1')

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
    
