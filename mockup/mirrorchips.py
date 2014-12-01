def mirror(player):
    center = 400
    new_stack = []
    for chip in player:
        dx = chip[0] - center
        # new_x = center - dx - 11
        new_x = chip[0] - 187
        # new_y = chip[1] + 125
        new_y = chip[1] - 12
        # new_stack.append([new_x, chip[1]])
        new_stack.append([new_x, new_y])
    print new_stack
    
p1 = [[494, 90], [475, 92], [488, 106], [507, 104], [470, 108]]
p2 = [[644, 132], [630, 142], [648, 149], [631, 160], [647, 167]]
p8 = [[145, 132], [159, 142], [141, 149], [158, 160], [142, 167]]
p5 = [[395, 345], [378, 340], [412, 340], [362, 345], [429, 345]]
# mirror(p5)

player4_center = (582, 333)
player6_center = (208, 333)

def mirror_button(button):
    center = 400
    dx = button[0] - center
    new_x = center - dx - 15
    print new_x, button[1]

b1 = (607, 105)

mirror_button(b1)  


    
