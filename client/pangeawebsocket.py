from decimal import Decimal
import random
import json
from ws4py.websocket import WebSocket

cards = ["2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "JC", "QC", "KC", "AC", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD", "AD", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "JH", "QH", "KH", "AH", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "JS", "QS", "KS", "AS"]

class PangeaWebSocket(WebSocket):
    def __init__(self, sock, protocols=None, extensions=None, environ=None, heartbeat_freq=None):
        super(PangeaWebSocket, self).__init__(sock, protocols=None, extensions=None, environ=None, heartbeat_freq=None)
        self.default_usernames = ['kuphephaw6','Pantiwx','duvaye62','albogawx','oklepankal6','aikokj','immoseut','dixibelonly1wu','possano9s','claireneubertj9','Schwerinoa','jorsonwa','atheistafghanfa','fliblySnallbr','outflowbs','ege1mee6','hondan87','espasasp4','mietlicada','grasog4q']
        self.usernames = list(self.default_usernames)
        self.playerseat = self.make_empty_player()
        self.empty_seat = {'empty':1, 'playing':0, 'playercards':None, 'stack':None, 'action':''}
        self.emptyseats = self.make_empty_seats()
        self.seats = self.emptyseats.copy()
        self.player = None

    def blank_cards(self):
        for seat in self.seats.keys():
            self.seats[seat]['playercards'] = None
            print self.seats[seat]
        
    def make_empty_player(self):
        return {'name':'LauraPalmer', 'stack':self.get_stack(), 'empty':0, 'playing':1, 'player':1, 'playercards':None}
    
    def make_empty_seats(self):
        theseseats = {}
        for i in range(9):
            theseseats[i] = self.empty_seat
        return theseseats

    def get_player(self):
        name = self.usernames[random.randint(0, len(self.usernames)-1)]
        self.usernames.remove(name)
        return name

    def get_stack(self):
        stack = random.randint(100, 100000) * .01
        return float(Decimal(stack).quantize(Decimal('.01')))

    def get_active(self):
        active = []
        for key in self.seats.keys():
            if self.seats[key]['empty'] != 1: active.append(key)
        return active

    def get_dealer(self):
        active = self.get_active()
        dealer = random.randrange(0, len(active))
        dealer = active[dealer]
        return dealer

    def get_card(self):
         return cards[random.randint(0,len(cards)-1)]
                            
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
        def clearseats(doesntmatter):
            self.player = None
            player_msg = {'seat':None, 'stack':0, 'sitting':0, 'holecards':[None, None]}
            self.send_message({'player':player_msg})
            self.seats = self.emptyseats.copy()
            self.send_all_seats()
            # player_msg = self.make_empty_player()
            # self.send_message({'player':player_msg})

        def deal1(doesnmatter):
            c = [None, None]
            if self.player != None:
                c = [self.get_card(), self.get_card()]
            self.send_message({'deal':{'holecards':[c[0], c[1]],
                                       'dealer':self.get_dealer()}})

        def deal2(x):
            self.send_message({'deal':{'board':{0:self.get_card(), 1:self.get_card(), 2:self.get_card()}}})
        def deal3(x):
            self.send_message({'deal':{'board':{3:self.get_card()}}})
        def deal4(x):
            self.send_message({'deal':{'board':{4:self.get_card()}}})
                                    
        def fillseats(num_players):
            # clearseats('yea')
            self.blank_cards()
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

        def showbets(yea):
            for seat in self.seats.keys():
                if self.seats[seat]['playing'] == 1:
                    this_bet = random.randint(1,int(self.seats[seat]['stack']))
                    self.seats[seat]['bet'] = this_bet
            self.send_all_seats()
                                        
        def showcards(doesntmatter):
            for seat in self.seats.keys():
                if self.seats[seat]['empty'] != 1:
                    self.seats[seat]['playercards'] = [self.get_card(), self.get_card()]
            self.send_all_seats()

        def potamount(new_amount):
            self.send_message({'game':{'pot':[str(new_amount)]}})

        def movetopot(yea):
            self.send_message({'action':{'chipsToPot':0}})

        def movetoplayer(seatnum):
            self.send_message({'action':{'chipsToPlayer':str(seatnum)}})

            
        handlers = {'clearseats':clearseats, 'fillseats':fillseats,
                    'deal1':deal1, 'showcards':showcards, 'deal2':deal2,
                    'deal3':deal3, 'deal4':deal4, 'showbets':showbets,
                    'potamount':potamount, 'movetopot':movetopot,
                    'movetoplayer':movetoplayer}

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
            self.blank_cards()
            self.send_all_seats()
            self.send_message({'player':player_msg})

        def fold(ok):
            self.send_message({'action':{'returnPlayerCards':str(self.player)}})
            
        handlers = {'join':join, 'fold':fold}
        for key in message.keys():
            if key in handlers.keys():
                handler = handlers[key]
                handler(message[key])
            else: self.error(key)

    def echo(self, echo_msg):
        self.send_message(echo_msg)
                                
    def received_message(self, message):
        print "Recieved: " + message.data
        message = json.loads(message.data)
        handlers = {'test':self.test, 'action':self.action, 'echo':self.echo}
        for key in message.keys():
            if key in handlers.keys():
                handler = handlers[key]
                handler(message[key])
            else: self.error(key)
