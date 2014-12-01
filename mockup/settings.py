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
    return (seat_angles, seat_attrs)
    
def layout2():
    seat_angles = [95, 30, 330,
                   272, 0, 0,
                   0, 0, 0]

    seat_attrs = {'height':80, 'width':105}
    return (seat_angles, seat_attrs)

def layout3():
    seat_angles = [95, 30, 330,
                   272, 0, 0,
                   0, 0, 0]

    seat_attrs = {'height':90, 'width':105}
    return (seat_angles, seat_attrs)


# seat_angles, seat_attrs = layout1()       
seat_angles, seat_attrs = layout2()

tablecardimgs = ['./images/cards/AS-70.png',
                  './images/cards/QS-70.png',
                  './images/cards/KH-70.png',
                  './images/cards/9C-70.png',
                  './images/cards/2D-70.png']

facecardimg = './images/cards/4C-150.png'

card_back = './images/cards/Red_Back-150.png'
# card_back = './images/cards/Blue_Back-150.png'

faceup_w = 150
c1top = '12px'
c1left = '15px'
c2top = '25px'
c2left = '40px'

table_config1 = {'faceup':[1,5,7],
                 'names':['snake', 'laurapalmer', 'drjacoby',
                          'agentcooper', 'audreyhorne', 'nadineH',
                          'deputyhawk', 'davidlynch', 'ronettepulaski'],
                 'amounts':['90.01', '2405.21', '100.00', '3102.00',
                            '689.78', '4.00', '1307.16', '8088.90',
                            '402.02']
}


avatarcolors = {'rainbow': ['#616f91','#262626','#d4c400',
                            '#500c09','#b14500','#05004f',
                            '#410062','#026100','#ffd8d8'],
                'pink': ['#ffd8d8','#ffd8d8','#ffd8d8','#ffd8d8',
                         '#ffd8d8','#ffd8d8','#ffd8d8','#ffd8d8',
                         '#ffd8d8'],
                'blue': ['#616f91','#616f91','#616f91','#616f91',
                         '#616f91','#616f91','#616f91','#616f91',
                         '#616f91'],
                'black': ['#262626','#262626','#262626','#262626',
                          '#262626','#262626','#262626','#262626',
                          '#262626']}

bgcolors = avatarcolors['pink']

default_avatar = './images/avatar-default.png'

stack_amounts = ['500.50', '45.00', '3417.99', '201', '1.00',
                 '1000.00', '1 Million', '67.77', '90.09']

actions = ['','Bet<br/>222.22','','','',
           '','','','Fold']

has_button = [1,2,3,4,5,6,7,8,9]

bgimage = "./images/bg-green.png"
# bgimage = "./images/bg.png"
