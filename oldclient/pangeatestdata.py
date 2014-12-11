import random

usernames = ['kuphephaw6','Pantiwx','duvaye62','albogawx','oklepankal6','aikokj','immoseut','dixibelonly1wu','possano9s','claireneubertj9','Schwerinoa','jorsonwa','atheistafghanfa','fliblySnallbr','outflowbs','ege1mee6','hondan87','espasasp4','mietlicada','grasog4q']

def get_player():
    name = usernames[random.randint(0, len(usernames-1))]
    stack = random.randint(100, 100000) * .01
    return (name, stack)
