from collections import OrderedDict
import settings as S

def render_css(cssrules):
    with open('static.css', 'r') as fh:
        css = fh.read()
    for selector in cssrules.keys():
        newcss = "\n%s {\n" % (selector)
        for prop in cssrules[selector]:
            newcss += "  %s:%s;\n" % (prop, cssrules[selector][prop])
        newcss += "}\n"
        css += newcss
    with open('seat-gradients.css', 'r') as fh2:
        bgs = fh2.read()
        css += bgs
    with open('pangeapoker.css', 'w') as fh3:
        fh3.write(css)

def add_rule(selector, prop, val, cssrules):
    if selector not in cssrules.keys():
        cssrules[selector] = {}
    cssrules[selector][prop] = val
            
def seat_coordinates(seats, cssrules):
    import math
    def on_ellipse(a, b, theta_degrees):
        """Give h radius (a), vertical radius (b), and angle in degrees,
        Get x,y of point on ellipse"""
        theta = math.radians(theta_degrees)
        x = (a*b / math.sqrt(b**2 + (a**2 * math.tan(theta)**2)))
        y = (a*b / math.sqrt(a**2 + (b**2 / math.tan(theta)**2)))
        if theta_degrees <= 90:
            return (x,-y)
        elif theta_degrees <= 180:
            return (-x, -y)
        elif theta_degrees <= 270:
            return (-x, y)
        else:
            return (x, y)

    def gettopleft(center_x, center_y, height,
                   width, ellipse_center=(400,225)):
        left = (center_x - width/2.0) + ellipse_center[0]
        top = center_y - height/2.0 + ellipse_center[1]
        return (left, top)

    def right_seat(seat):
        seat_center = on_ellipse(S.ellipse['hradius'],
                           S.ellipse['vradius'],
                           S.seat_angles[seat-1])
        seat_left, seat_top = gettopleft(seat_center[0], seat_center[1],
                                         S.seat_attrs['height'],
                                         S.seat_attrs['width'],
                                         S.ellipse['center'])
        if seat == 4:
            seat_top -= 10
        
        return (seat_left, seat_top)

    def center_seat(seat):
        centerX = S.table_center[0]
        centerY = 500 #this num doesn't matter
        seat_left  = gettopleft(centerX, centerY,
                                S.seat_attrs['height'],
                                S.seat_attrs['width'], (0,0))[0]
        seat_top = seat_coords[4][1] + (S.seat_attrs['height'] *
                                        S.center_seat_offset)
        return (seat_left, seat_top)

    def left_seat(seat):
        pairs = {6:4, 7:3, 8:2, 9:1}
        mirror = seat_coords[pairs[seat]]
        left_delta = mirror[0] - S.table_center[0]
        seat_left = S.table_center[0]-left_delta-S.seat_attrs['width']
        seat_top = mirror[1]
        return seat_left, seat_top

    seat_coords = {}
    for seat in seats:
        seat_positions = ['right','right','right','right','center',
                          'left','left','left','left']    
        if seat_positions[seat-1] == 'right':
            seat_left, seat_top = right_seat(seat)
        elif seat_positions[seat-1] == 'center':
            seat_left, seat_top = center_seat(seat)
        else:
            seat_left, seat_top = left_seat(seat)
        seat_coords[seat] = seat_left, seat_top
        selector = '#seat-%s' % (seat)
        add_rule(selector, 'left', str(seat_left) + 'px', cssrules)
        add_rule(selector, 'top', str(seat_top) + 'px', cssrules)
    return seat_coords
        
def seat_sizes(seats, cssrules):
    for seat in seats:
        selector = '#seat-%s' % (seat)
        add_rule(selector, 'height', S.seat_attrs['height'], cssrules)
        add_rule(selector, 'min-height', S.seat_attrs['height'], cssrules)
        add_rule(selector, 'width', S.seat_attrs['width'], cssrules)
        add_rule(selector, 'min-width', S.seat_attrs['width'], cssrules)

def player_cards(seats, cssrules):
    faceup_sel = '.faceup > img'
    faceup_width = str(S.faceup_w) + 'px'
    add_rule(faceup_sel, 'width', faceup_width, cssrules)
    card1 = '.card1'
    card2 = '.card2'
    add_rule(card1, 'top', S.c1top, cssrules)
    add_rule(card1, 'left', S.c1left, cssrules)
    add_rule(card2, 'top', S.c2top, cssrules)
    add_rule(card2, 'left', S.c2left, cssrules)

def stack_labels(seats, seat_coords, cssrules):
    seat_pos = ['top', 'top', 'bottom', 'bottom', 'bottom',
                'bottom', 'bottom', 'top', 'top']
    for seat in seats:
        position = seat_pos[seat-1]
        if position == 'top':
            top = seat_coords[seat][1] + 83
        else:
            top = seat_coords[seat][1] - 12
        left = seat_coords[seat][0]
        selector = '#stack%s' % (seat)
        add_rule(selector, 'top', top, cssrules)
        add_rule(selector, 'left', left, cssrules)

def bg_image(cssrules):
    selector = '#poker-room'
    image = S.bgimage
    val = "url('%s')" % image
    add_rule(selector, 'background-image', val, cssrules)
            
cssrules = OrderedDict()
seats = range(10)[1:]
bg_image(cssrules)
seat_coords = seat_coordinates(seats, cssrules)
seat_sizes(seats, cssrules)
player_cards(seats, cssrules)
stack_labels(seats, seat_coords, cssrules)
render_css(cssrules)

