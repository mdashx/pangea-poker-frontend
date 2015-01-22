import json
from ws4py.websocket import WebSocket
from sample_games import game_one

class SampleGameOne(WebSocket):
    def __init__(self, sock, protocols=None, extensions=None, environ=None, heartbeat_freq=None):
        super(SampleGameOne, self).__init__(sock, protocols=None, extensions=None, environ=None, heartbeat_freq=None)
        self.commands = game_one.__iter__()
        
    def received_message(self, message):
        next_command = self.commands.next()
        send_message = json.dumps(next_command)
        print send_message
        self.send(send_message)
        
