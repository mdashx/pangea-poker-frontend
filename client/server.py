# https://ws4py.readthedocs.org/en/latest/sources/servertutorial/
# http://stackoverflow.com/questions/8125507/how-can-i-send-and-receive-websocket-messages-on-the-server-side

from wsgiref.simple_server import make_server
from ws4py.server.wsgirefserver import WSGIServer, WebSocketWSGIRequestHandler
from ws4py.server.wsgiutils import WebSocketWSGIApplication
from pangeawebsocket import PangeaWebSocket
from api_example import SampleGameOne


# PangeaWebSocket
myserver = PangeaWebSocket
# SampleGameOne
# myserver = SampleGameOne


server = make_server('', 9000, server_class=WSGIServer,
                     handler_class=WebSocketWSGIRequestHandler,
                     app=WebSocketWSGIApplication(handler_cls=myserver))






server.initialize_websockets_manager()
server.serve_forever()
