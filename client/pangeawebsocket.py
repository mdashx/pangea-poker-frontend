from decimal import Decimal
import random
import json
from ws4py.websocket import WebSocket

class PangeaWebSocket(WebSocket):
    def __init__(self, sock, protocols=None, extensions=None, environ=None, heartbeat_freq=None):
        super(PangeaWebSocket, self).__init__(sock, protocols=None, extensions=None, environ=None, heartbeat_freq=None)
        self.default_usernames = ['kuphephaw6','Pantiwx','duvaye62','albogawx','oklepankal6','aikokj','immoseut','dixibelonly1wu','possano9s','claireneubertj9','Schwerinoa','jorsonwa','atheistafghanfa','fliblySnallbr','outflowbs','ege1mee6','hondan87','espasasp4','mietlicada','grasog4q']
        self.usernames = list(self.default_usernames)
        self.playerseat = {'name':'LauraPalmer', 'stack':self.get_stack(), 'empty':0, 'playing':1, 'player':1}
        self.emptyseats = {0:{'empty':1}, 1:{'empty':1}, 2:{'empty':1}, 3:{'empty':1}, 4:{'empty':1}, 5:{'empty':1}, 6:{'empty':1}, 7:{'empty':1}, 8:{'empty':1}}
        self.seats = self.emptyseats.copy()
        self.player = None

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
        print self.seats
        for seat in self.seats.keys():
            this_seat = {'seat':seat}
            this_seat.update(self.seats[seat])
            these_seats.append(this_seat)
        self.send_message({'seats':these_seats})
        
    def test(self, message):
        def fillseats(num_players):
            if not isinstance(num_players, int): num_players = 9
            if num_players < 0 or num_players > 9: num_players = 9
            self.usernames = list(self.default_usernames)
            self.seats = self.emptyseats.copy()
            these_seats = range(0,9)
            print these_seats
            if self.player in range(0,9):
                self.seats[self.player] = self.playerseat
                these_seats.remove(self.player)
                num_players -= 1
            for i in range(num_players):
                print these_seats
                this_seat = random.randrange(0, len(these_seats))
                new_seat = these_seats[this_seat]
                these_seats.remove(new_seat)
                self.seats[new_seat] = {'name':self.get_player(), 'stack':self.get_stack(), 'empty':0, 'playing':1}
            self.send_all_seats()

        def clearseats(doesntmatter):
            self.seats = self.emptyseats.copy()
            self.send_all_seats()
            player_msg = {'seat':'', 'stack':'', 'sitting':0}
            self.send_message({'player':player_msg})

        def deal1(doesnmatter):
            if self.player != None:
                c1 = "AS"
                c2 = "AD"
                self.send_message({'player':{'holecards':[c1, c2]}})
                self.send_message({'action':{'deal':'holecards'}})

        handlers = {'clearseats':clearseats, 'fillseats':fillseats,
                    'deal1':deal1}      

        for key in message.keys():
            if key in handlers.keys():
                handler = handlers[key]
                handler(message[key])
            else: self.error(key)
            
    def action(self, message):
        def join(seat):
            self.player = seat
            self.seats[seat] = self.playerseat
            player_msg = {'seat':seat, 'stack':self.playerseat['stack'], 'sitting':1}
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
