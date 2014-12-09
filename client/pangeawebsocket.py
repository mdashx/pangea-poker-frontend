from decimal import Decimal
import random
import json
from ws4py.websocket import WebSocket

usernames = ['kuphephaw6','Pantiwx','duvaye62','albogawx','oklepankal6','aikokj','immoseut','dixibelonly1wu','possano9s','claireneubertj9','Schwerinoa','jorsonwa','atheistafghanfa','fliblySnallbr','outflowbs','ege1mee6','hondan87','espasasp4','mietlicada','grasog4q']

def get_player():
    name = usernames[random.randint(0, len(usernames)-1)]
    usernames.remove(name)
    return name

def get_stack():
    stack = random.randint(100, 100000) * .01
    return float(Decimal(stack).quantize(Decimal('.01')))
    
player = {'name':'LauraPalmer', 'stack':get_stack()}
seats = {0:{}, 1:{}, 2:{}, 3:{}, 4:{}, 5:{}, 6:{}, 7:{}, 8:{}}

def add_seats(update_seats):
    these_seats = []
    for seat in update_seats:
        this_seat = {'seat':seat}
        this_seat.update(seats[seat])
        these_seats.append(this_seat)
    return these_seats

class PangeaWebSocket(WebSocket):
    def send_message(self, send_message):
        send_message = json.dumps(send_message)
        print "Sending: " + send_message
        self.send(send_message)

    def error(self, message):
        self.send("Message not recognized: " + message)

    def send_all_seats(self):
        these_seats = []
        for seat in seats.keys():
            this_seat = {'seat':seat}
            this_seat.update(seats[seat])
            these_seats.append(this_seat)
        self.send_message({'seats':these_seats})
        
    def test(self, message):
        if message == 'fillseats':
            for seat in seats.keys():
                if seats[seat] == {}:
                    seats[seat] = {'name':get_player(), 'stack':get_stack()}
            self.send_all_seats()

    def action(self, message):
        def join(seat):
            seats[seat] = player
            seat_msg = add_seats([seat])
            player_msg = {'seat':seat, 'stack':player['stack']}
            # self.send_message({'seats':seat_msg})
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
