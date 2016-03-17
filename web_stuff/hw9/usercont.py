# Ashley Towne
# Users Controller

import json
import cherrypy

class UserController():
    def __init__(self, mdb):
        self.mdb = mdb

    def GET(self, key):
        key = int(key)
        output = {'result':'success'}
        try:
            output['gender'] = self.mdb.users[key]['gender']
            output['age'] = self.mdb.users[key]['age']
            output['zipcode'] = self.mdb.users[key]['zipcode']
            output['id'] = key
            output['occupation'] = int(self.mdb.users[key]['occupation'])
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
            userlist = []
            for k in self.mdb.users.keys():
                try:
                    userlist.append(
                        {'result':'success',
                        'gender':self.mdb.users[int(k)]['gender'],
                        'age':self.mdb.users[int(k)]['age'],
                        'zipcode':self.mdb.users[int(k)]['zipcode'],
                        'id':int(k),
                        'occupation':int(self.mdb.users[int(k)]['occupation'])}
                        )
                except Exception as ex:
                    userlist.append({'result':'error',
                        'message':ex})
            output['users'] = userlist
        except Exception as ex:
            otuput['result'] = 'error'
            output['message'] = ex
        return json.dumps(output, encoding='latin-1')

    def POST(self):
        output = {'result':'success'}
        try:
            instr = cherrypy.request.body.read()
            indict = json.loads(instr)
            new_id = max([int(k) for k in self.mdb.users.keys()]) + 1
            self.mdb.set_user(new_id, [indict['gender'], indict['age'], indict['occupation'], indict['zipcode']])
            output['id'] = int(new_id)
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = ex
        return json.dumps(output, encoding='latin-1')

    def PUT(self, key):
        output = {'result':'success'}
        instr = cherrypy.request.body.read()
        indict = json.loads(instr)
        try: 
            self.mdb.set_user(int(key), [indict['gender'], indict['age'], indict['occupation'], indict['zipcode']])
            output['id'] = int(key)
        except KeyError as ex:
            output['result'] = 'error'
            output['message'] = 'key not found'
        return json.dumps(output, encoding='latin-1')

    def DELETE(self, key):
        output = {'result':'success'}
        try:
            del self.mdb.users[int(key)]
            output['message'] = "key {i} deleted".format(i=key)
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = ex
        return json.dumps(output, encoding='latin-1')

    def DELETE_ALL(self):
        output = {'result':'success'}
        try:
            self.mdb.users.clear()
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = ex
        return json.dumps(output, encoding='latin-1')

