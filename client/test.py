import json

a = {'seat':0, 'name':'drjacoby', 'stack':666.09, 'avatar':'./images/avatar-default2.png'}

b = {'seat':1, 'name':'snake', 'stack':304.08, 'action':'Bet<br>200.01'}

test_seats = [a, b]

print json.dumps({'seats':test_seats})
