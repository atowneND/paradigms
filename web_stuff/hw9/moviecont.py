# Ashley Towne
# Movie Controller

import json
import cherrypy

class MovieController():
    def __init__(self, mdb):
        self.mdb = mdb

    def GET(self, key):
        key = str(key)
        output = {'result':'success'}
        try:
            output['key'] = key
            output['value'] = self.mdb.movies[int(key)]
        except KeyError as ex:
            output['result'] = 'error'
            output['message'] = 'key not found'
        return json.dumps(output, encoding='latin-1')

    def GET_ALL(self):
        output = {'result':'success'}
        output['entries'] = [
            {"key": k, "value": v} for k, v in self.mdb.movies.iteritems()
        ]
        return json.dumps(output, encoding='latin-1')

    def POST(self):
        output = {'result':'success'}
        instr = cherrypy.request.body.read()
        indict = json.loads(instr)
        try:
            self.mdb.movies[int(indict['key'])] = indict['value']
        except KeyError as ex:
            output['result'] = 'error'
            output['message'] = 'key not found'
        return json.dumps(output, encoding='latin-1')


    def PUT(self, key):
        output = {'result':'success'}
        instr = cherrypy.request.body.read()
        indict = json.loads(instr)
        try: 
            self.mdb.movies[int(key)] = indict['value'] 
        except KeyError as ex:
            output['result'] = 'error'
            output['message'] = 'key not found'
        return json.dumps(output, encoding='latin-1')

    def DELETE(self, key):
        output = {'result':'success'}
        if int(key) not in self.mdb.movies:
            output['result'] = 'error'
            output['message'] = 'key not found'
        else:
            del self.mdb.movies[int(key)]
            output['message'] = "key {i} deleted".format(i=key)
        return json.dumps(output, encoding='latin-1')

    def DELETE_ALL(self):
        output = {'result':'success'}
        self.mdb.movies.clear()
        return json.dumps(output, encoding='latin-1')

