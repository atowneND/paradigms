# Ashley Towne
# Reset Controller

import json
import cherrypy

class ResetController():
    def __init__(self, mdb):
        self.mdb = mdb

    def PUT(self, key):
        output = {'result':'success'}
        print 'hi'
#        self.mdb.load_one_movie('ml-1m/movies.dat',int(key))
        return json.dumps(output, encoding='latin-1')

    def PUT_ALL(self):
        output = {'result':'success'}
        print 'yo'
#        self.mdb.__init__()
#        self.mdb.load_movies('ml-1m/movies.dat')
#        self.mdb.load_users('ml-1m/users.dat')
#        self.mdb.load_ratings('ml-1m/ratings.dat')
        return json.dumps(output, encoding='latin-1')

