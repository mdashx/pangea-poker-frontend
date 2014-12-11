from decimal import Decimal
import random
import json
from ws4py.websocket import WebSocket

class PangeaWebSocket(WebSocket):
    def __init__(self, sock, protocols=None, extensions=None, environ=None, heartbeat_freq=None):
        super(PangeaWebSocket, self).__init__(sock, protocols=None, extensions=None, environ=None, heartbeat_freq=None)
        self.default_usernames = ['kuphephaw6','Pantiwx','duvaye62','albogawx','oklepankal6','aikokj','immoseut','dixibelonly1wu','possano9s','claireneubertj9','Schwerinoa','jorsonwa','atheistafghanfa','fliblySnallbr','outflowbs','ege1mee6','hondan87','espasasp4','mietlicada','grasog4q']
        self.usernames = list(self.default_usernames)
        self.player = {'name':'LauraPalmer', 'stack':self.get_stack(), 'empty':0}
        self.emptyseats = {0:{'empty':1}, 1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{}, 8:{}}
        self.seats = self.emptyseats.copy()

    def get_player(self):
        name = self.usernames[random.randint(0, len(self.usernames)-1)]
        self.usernames.remove(name)
        return name

    def get_stack(self):
        stack = random.randint(100, 100000) * .01
        return float(Decimal(stack).quantize(Decimal('.01')))
                    
    def send_message(self, send_message):
        send_message = json.dumps(send_message)
        print "Sending: " + send_message
        self.send(send_message)

    def error(self, message):
        self.send("Message not recognized: " + message)

    def send_all_seats(self):
        these_seats = []
        for seat in self.seats.keys():
            this_seat = {'seat':seat}
            this_seat.update(self.seats[seat])
            these_seats.append(this_seat)
        self.send_message({'seats':these_seats})
        
    def test(self, message):
        if message == 'fillseats':
            for seat in self.seats.keys():
                if self.seats[seat] == {}:
                    self.seats[seat] = {'name':self.get_player(), 'stack':self.get_stack()}
            self.send_all_seats()
        if message == 'clearseats':
            self.seats = self.emptyseats.copy()
            self.send_all_seats()
            
    def action(self, message):
        def join(seat):
            self.seats[seat] = self.player
            player_msg = {'seat':seat, 'stack':self.player['stack']}
            self.send_all_seats()
            self.send_message({'player':player_msg})
                        
        handlers = {'join':join}
        for key in message.keys():
            if key in handlers.keys():
                handler = handlers[key]
                handler(message[key])
            else: self.error(key)
                
    def received_message(self, message):
        print "Recieved: " + message.data
        message = json.loads(message.data)
        handlers = {'test':self.test, 'action':self.action}
        for key in message.keys():
            if key in handlers.keys():
                handler = handlers[key]
                handler(message[key])
            else: self.error(key)
            
        # if message.data == 'test':
        #     send_message = json.dumps({'seats':test_seats})
        #     self.send_message(send_message)
        # if message.data
