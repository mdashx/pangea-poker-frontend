table_center = (400, 225)

# ellipse = {'center':(400,230), 'hradius':320, 'vradius':190}
# ellipse = {'center':(500,230), 'hradius':320, 'vradius':190}

# From inkscape: hradius: 152.73508, vradius: 171.82695
# cy: 242.23399999999998, cx: 581.726

# ellipse = {'center':(581, 242), 'hradius':153, 'vradius':172}
ellipse = {'center':(581, 230), 'hradius':153, 'vradius':172}

# seat_angles = [40, 10, 345,
#                315, 270, 225,
#                185, 160, 130]

seat_angles = [90, 30, 339,
               280, 270, 225,
               185, 160, 130]

# seat_attrs = {'height':90, 'width':110}
seat_attrs = {'height':80, 'width':105}


# percentage of seat height
center_seat_offset = .15

def layout1():
    seat_angles = [90, 30, 339,
                   280, 270, 225,
                   185, 160, 130]
    
    seat_attrs = {'height':90, 'width':110}
    
def layout2():
    seat_angles = [95, 30, 330,
                   272, 0, 0,
                   0, 0, 0]

    seat_attrs = {'height':80, 'width':105}
    return (seat_angles, seat_attrs)
    
seat_angles, seat_attrs = layout2()

tablecardimgs = ['./images/cards/AS.png',
                  './images/cards/AS.png',
                  './images/cards/AS.png',
                  './images/cards/AS.png',
                  './images/cards/AS.png']

facecardimg = './images/cards/AS.png'

faceup_w = 150
c1top = '12px'
c1left = '15px'
c2top = '25px'
c2left = '40px'

