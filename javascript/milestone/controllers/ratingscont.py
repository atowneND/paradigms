# Ashley Towne
# Users Controller

import json
import cherrypy

class RatingsController():
    def __init__(self, mdb):
        self.mdb = mdb

    def GET(self, key):
        key = int(key)
        output = {'result':'success'}
        try:
            output['movie_id'] = key
            output['rating'] = self.mdb.get_rating(key)
        except KeyError as ex:
            output['result'] = 'error'
            output['message'] = 'key not found'
        return json.dumps(output, encoding='latin-1')

