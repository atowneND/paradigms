# Ashley Towne
# Users Controller

import json
import cherrypy

class RecsController():
    def __init__(self, mdb):
        self.mdb = mdb

    def GET(self, key):
        key = int(key)
        output = {'result':'success'}
        try:
            mid = self.mdb.get_recommended_movie(key)
            output['movie_id'] = int(mid)
        except KeyError as ex:
            output['result'] = 'error'
            output['message'] = 'key not found'
        return json.dumps(output, encoding='latin-1')

    def PUT(self, key):
        output = {'result':'success'}
        try: 
            instr = cherrypy.request.body.read()
            indict = json.loads(instr)
            print indict['rating']
            self.mdb.set_user_movie_rating(key, indict['movie_id'], indict['rating'])
        except KeyError as ex:
            output['result'] = 'error'
            output['message'] = 'key not found'
        return json.dumps(output, encoding='latin-1')

    def DELETE(self):
        output = {'result':'success'}
        try:
            self.mdb.delete_all_ratings()
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = ex
        return json.dumps(output, encoding='latin-1')

