import json
import cherrypy

class DictionaryController():
    def __init__(self):
        self.myd = dict()

    def GET(self, key):
        key = str(key)
        output = {'result':'success'}
        try:
            output['key'] = key
            output['value'] = self.myd[key]
        except KeyError as ex:
            output['result'] = 'error'
            output['message'] = 'key not found'
        return json.dumps(output, encoding='latin-1')

    def GET_ALL(self):
        output = {'result':'success'}
        output['entries'] = [
            {"key": k, "value": v} for k, v in self.myd.iteritems()
        ]
        return json.dumps(output, encoding='latin-1')

    def POST(self):
        output = {'result':'success'}
        instr = cherrypy.request.body.read()
        indict = json.loads(instr)
        try:
            self.myd[str(indict['key'])] = indict['value']
        except KeyError as ex:
            output['result'] = 'error'
            output['message'] = 'key not found'
        return json.dumps(output, encoding='latin-1')


    def PUT(self, key):
        output = {'result':'success'}
        instr = cherrypy.request.body.read()
        indict = json.loads(instr)
        try: 
            self.myd[str(key)] = indict['value'] 
        except KeyError as ex:
            output['result'] = 'error'
            output['message'] = 'key not found'
        return json.dumps(output, encoding='latin-1')

    def DELETE(self, key):
        output = {'result':'success'}
        if key not in self.myd:
            output['result'] = 'error'
            output['message'] = 'key not found'
        else:
            del self.myd[str(key)]
            output['message'] = "key {i} deleted".format(i=key)
        return json.dumps(output, encoding='latin-1')

    def DELETE_ALL(self):
        output = {'result':'success'}
        self.myd.clear()
        return json.dumps(output, encoding='latin-1')
