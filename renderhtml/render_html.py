import lxml.html
import static

def render_html(html):
    with open('index.html', 'w') as fh:
        out = lxml.html.tostring(html, pretty_print=True)
        fh.write(out)

def get_static_html():
    with open('static.html', 'r') as fh:
        static_html = fh.read()
    html = lxml.html.fromstring(static_html)
    return html    

def add_seats(seats, html):
    def add_action_label(seat, thisseat):
        labelid = 'seat%saction' % (seat)
        label = lxml.html.Element('div')
        label.attrib.update({'class':'action', 'id':labelid})
        thisseat.append(label)

    def add_stack_label(seat, pokerroom):
        stack_id = "stack%s" % (seat)
        thisstack = lxml.html.Element('div')
        thisstack.attrib.update({'class':'stack-label', 'id':stack_id})
        center = lxml.html.Element('center')
        span = lxml.html.Element('span')
        spanid = "stack%sspan" % (seat)
        span.attrib.update({'id':spanid})
        center.append(span)
        thisstack.append(center)
        pokerroom.append(thisstack)
        return pokerroom
        
    def add_seat(seat, pokerroom):
        seat_id = "seat-%s" % (seat)
        thisseat = lxml.html.Element('div')
        thisseat.attrib.update({'class':'player-info', 'id':seat_id})
        pokerroom.append(thisseat)
        return (pokerroom, thisseat)

    pokerroom = html.get_element_by_id('poker-room')
    for seat in seats:
        pokerroom, thisseat = add_seat(seat, pokerroom)
        pokerroom = add_stack_label(seat, pokerroom)
        add_action_label(seat, thisseat)

def add_facedown_cards(seats, html):
    for seat in seats:
        seat_id = "seat-%s" % (seat)
        thisseat = html.get_element_by_id(seat_id)
        info = thisseat.find_class('player-info')[0]
        down1 = lxml.html.Element('div')
        down1.attrib.update({'class':'facedown down0'})
        down2 = lxml.html.Element('div')
        down2.attrib.update({'class':'facedown down1'})
        info.append(down1)
        info.append(down2)

def add_faceup_cards(seats, html):
    for seat in seats:
        seat_id = "seat-%s" % (seat)
        card1_id = "seat%scard0" % (seat)
        card2_id = "seat%scard1" % (seat)
        card1 = lxml.html.Element('div')
        card1.attrib.update({'id':card1_id, 'class':'faceup card0'})
        card2 = lxml.html.Element('div')
        card2.attrib.update({'id':card2_id, 'class':'faceup card1'})
        thisseat = html.get_element_by_id(seat_id)
        thisseat.append(card1)
        thisseat.append(card2)
        static_html = '<div class="invitation"><center>Sit Down</center></div>'
        invite = lxml.html.fromstring(static_html)
        thisseat.append(invite)

def add_status(seats, html):
    for seat in seats:
        seat_id = "seat-%s" % (seat)
        status = lxml.html.Element('div')
        status.attrib.update({'class':'player-status'})
        playername = lxml.html.Element('span')
        playername.attrib.update({'class':'player-name'})
        playername.text = 'Anonymous'
        playeramount = lxml.html.Element('span')
        playeramount.attrib.update({'class':'player-amount'})
        playeramount.text = '0.00'
        status.append(playername)
        status.append(lxml.html.Element('br'))
        status.append(playeramount)
        thisseat = html.get_element_by_id(seat_id)
        thisseat.append(status)

def add_buttons(buttons, html):
    labels = ['fold', 'check', 'bet']
    pokerroom = html.get_element_by_id('poker-room')
    for button in buttons:
        btn = lxml.html.Element('div')
        btn.attrib.update({'class':'btn', 'id':labels[button]})
        btn.text = labels[button].capitalize()
        pokerroom.append(btn)

def add_slider(html):
    pokerroom = html.get_element_by_id('poker-room')
    slider = lxml.html.Element('input')
    attr = {'id':'bet_slider', 'type':'range', 'min':'0',
            'max':'1000','value':'1', 'step':'1'}
    slider.attrib.update(attr)
    pokerroom.append(slider)

def amount_input(html):
    pokerroom = html.get_element_by_id('poker-room')
    label = lxml.html.Element('span')
    label.attrib.update({'id':'bet-label'})
    label.text = "Bet Amount:"
    pokerroom.append(label)
    txtinput = lxml.html.Element('input')
    txtinput.attrib.update({'type':'text', 'id':'bet-amount'})
    pokerroom.append(txtinput)

def add_static(html, static_html):
    pokerroom = html.get_element_by_id('poker-room')
    new_html = lxml.html.fromstring(static_html)
    for child in new_html.iterchildren():
        pokerroom.append(child)

def add_dealer_button(html, seat):
    pokerroom = html.get_element_by_id('poker-room')
    element_id = "seat%sbutton" % (seat)
    dealerbtn = lxml.html.Element('div')
    dealerbtn.attrib.update({'class':'dealerbutton', 'id':element_id})
    dealerbtn.text = "D"
    pokerroom.append(dealerbtn)

def add_dealer_buttons(html):
    for seat in seats:
        add_dealer_button(html, seat)
        
seats = range(9)
buttons = range(3)
html = get_static_html()
add_seats(seats, html)
add_facedown_cards(seats, html)
add_status(seats, html)
add_faceup_cards(seats, html)
add_buttons(buttons, html)
add_slider(html)
amount_input(html)
add_static(html, static.autocontrols)
add_static(html, static.infobox)
add_dealer_buttons(html)


## Render HTML

render_html(html)
