# Ashley Towne
# Users Controller

import json
import cherrypy

class RatingsController():
    def __init__(self, mdb):
        self.mdb = mdb

    def GET(self, key):
        key = str(key)
        output = {'result':'success'}
        try:
            output['key'] = key
            output['value'] = self.mdb.users[int(key)]
        except KeyError as ex:
            output['result'] = 'error'
            output['message'] = 'key not found'
        return json.dumps(output, encoding='latin-1')

