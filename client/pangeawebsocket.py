from ws4py.websocket import WebSocket

class PangeaWebSocket(WebSocket):
    def received_message(self, message):
        if message.data == 'cat':
            print message.data
            print "it is a cat"
            self.send('dog', message.is_binary)
        else:
            self.send(message.data, message.is_binary)

