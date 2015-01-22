# seats = {'seats':{'name':'CvSdirtybSF', 'playing':1, 'stack':689.00, 'holecards':[None, None]}}

seats = {"seats": [{"stack": 563.67, "empty": 0, "playing": 1, "name": "espasasp4", "seat": 0}, {"stack": 397.32, "empty": 0, "playing": 1, "name": "aikokj", "seat": 1}, {"stack": 712.93, "empty": 0, "playing": 1, "name": "hondan87", "seat": 2}, {"stack": 93.83, "empty": 0, "playing": 1, "name": "mietlicada", "seat": 3}, {"stack": 197.88, "empty": 0, "playing": 1, "name": "outflowbs", "seat": 4}, {"stack": 66.82, "empty": 0, "playing": 1, "name": "duvaye62", "seat": 5}, {"stack": 285.65, "empty": 0, "playing": 1, "name": "possano9s", "seat": 6}, {"stack": 254.9, "empty": 00, "playing": 1, "name": "fliblySnallbr", "seat": 7}, {"stack": 2.34, "empty": 0, "playing": 1, "name": "oklepankal6", "seat": 8}]}

dealhole = {"deal": {"holecards": [None, None], "dealer": 0}}

pot = 0

"""
For all of these functions `clear` must be a list of seats to clear.
Ex: [3,4] or [3] or [1,2,6]
"""

def clear_actions(clear):
    clear_seats = []
    for seat in clear:
        this_seat = {'seat':seat, 'action':''}
        clear_seats.append(this_seat)
    return clear_seats

def fold(seat, clear=[]):
    msg = {'action':{'returnPlayerCards':str(seat)}, 'seats':[{'seat':seat, 'action':'<span>Fold</span>'}]}
    msg['seats'] += clear_actions(clear)
    return msg

def muck(seat, clear=[]):
    msg = {'action':{'returnPlayerCards':str(seat)}, 'seats':[{'seat':seat, 'action':'<span>Muck</span>'}]}
    msg['seats'] += clear_actions(clear)
    return msg
        
def bet(seat, bet, clear=[]):
    global pot
    pot = pot + bet
    msg = {'seats': [{'seat': seat, 'bet':bet, 'action':'<span>Bet<br>' + str(bet) + '</span>'}], 'game':{'pot':[str(pot)], 'tocall':bet}}
    msg['seats'] += clear_actions(clear)
    return msg
    
def call(seat, bet, clear=[]):
    global pot
    pot = pot + bet
    msg = {'seats': [{'seat': seat, 'bet':bet, 'action':'<span>Call<br>' + str(bet) + '</span>'}], 'game':{'pot':[str(pot)]}}
    msg['seats'] += clear_actions(clear)
    return msg

def _raise(seat, bet, clear=[]):
    global pot
    pot = pot + bet
    msg = {'seats': [{'seat': seat, 'bet':bet, 'action':'<span>Raise<br>' + str(bet) + '</span>'}], 'game':{'pot':[str(pot)], 'tocall':bet}}
    msg['seats'] += clear_actions(clear)
    return msg

def check(seat, clear=[]):
    global pot
    bet = 0
    msg = {'seats': [{'seat': seat, 'bet':bet, 'action':'<span>Check<br></span>'}]}
    msg['seats'] += clear_actions(clear)
    return msg



chips_in = {'seats':[{'seat':0, 'action':''}, {'seat':1, 'action':''}, {'seat':2, 'action':''},
                {'seat':3, 'action':''}, {'seat':4, 'action':''}, {'seat':5, 'action':''},
                {'seat':6, 'action':''}, {'seat':7, 'action':''}, {'seat':8, 'action':''}],
                'action':{'chipsToPot':0}}    

bets1 = [bet(0, 6), fold(1), call(2, 6, [1]), call(3, 6), fold(4), fold(5, [4]), fold(6, [5]), fold(7, [6]), _raise(8, 24, [7]), fold(0), call(2, 24, [0]), fold(3)]
deal2 = {'deal':{'board':{0:'AH', 1:'2C', 2:'6S'}}}
bets2 = [check(2), bet(8,24), call(2, 24)]
deal3 = {'deal':{'board':{3:'6H'}}}
bets3 = [check(2), check(8)]
deal4 = {'deal':{'board':{4:'JD'}}}
bets4 = [bet(2, 48), _raise(8, 72), call(2, 72)]


setup_game = {'game':{'pot':[0], 'bigblind':3, 'gametype':"NL Hold'em<br>Blinds: 3/6", 'tocall':0}}

game_one = [setup_game, seats, dealhole]

for message in bets1:
    game_one.append(message)

game_one += [chips_in, deal2]    
    
for message in bets2:
    game_one.append(message)

game_one += [chips_in, deal3]

for message in bets3:
    game_one.append(message)

game_one += [chips_in, deal4]
    
for message in bets4:
    game_one.append(message)

showdown = [{'seats':{'seat':2, 'playercards':['2H', '2D']}}, muck(8)]

game_one += showdown
