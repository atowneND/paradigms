# Ashley Towne
# 3/4/2016
# cherrypy primer

import cherrypy
from dcont import DictionaryController

def start_service():
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

    cherrypy.quickstart(app)

if __name__ == '__main__':
    start_service()
