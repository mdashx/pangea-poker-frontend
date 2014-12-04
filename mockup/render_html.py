import lxml.html
import settings as S
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
    return html

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
    return html

def add_names(seats, names, html):
    for seat in seats:
        seat_id = "seat-%s" % (seat)
        thisseat = html.get_element_by_id(seat_id)
        thisname = thisseat.find_class('player-name')[0]
        thisname.text =  names[seat-1]

def add_amounts(seats, amounts, html):
    for seat in seats:
        seat_id = "seat-%s" % (seat)
        thisseat = html.get_element_by_id(seat_id)
        thisamount = thisseat.find_class('player-amount')[0]
        thisamount.text =  amounts[seat-1]

def add_facedown_cards(seats, html):
    for seat in seats:
        seat_id = "seat-%s" % (seat)
        thisseat = html.get_element_by_id(seat_id)
        info = thisseat.find_class('player-info')[0]
        down1 = lxml.html.Element('div')
        down1.attrib.update({'class':'facedown down1'})
        down2 = lxml.html.Element('div')
        down2.attrib.update({'class':'facedown down2'})
        info.append(down1)
        info.append(down2)

def deal_facedown(seats, html):
    for seat in seats:
        seat_id = "seat-%s" % (seat)
        thisseat = html.get_element_by_id(seat_id)
        down1 = thisseat.find_class('down1')[0]
        down2 = thisseat.find_class('down2')[0]
        img1 = lxml.html.Element('img')
        img1.attrib.update({'src':S.card_back})
        img2 = lxml.html.Element('img')
        img2.attrib.update({'src':S.card_back})
        down1.append(img1)
        down2.append(img2)

def remove_facedown(seat, html):
    def remove_img(element):
        for child in element:
            element.remove(child)
    seat_id = "seat-%s" % (seat)
    thisseat = html.get_element_by_id(seat_id)
    down1 = thisseat.find_class('down1')[0]
    down2 = thisseat.find_class('down2')[0]
    remove_img(down1)
    remove_img(down2)
        
def add_tablecards(cards, html):
    def add_card(card, pokerroom):
        card_id = "card-%s" % (card)
        thiscard = lxml.html.Element('div')
        thiscard.attrib.update({'class':'tablecard', 'id':card_id})
        pokerroom.append(thiscard)
        return pokerroom
    pokerroom = html.get_element_by_id('poker-room')
    for card in cards:
        pokerroom = add_card(card, pokerroom)
    return html

def deal_tablecards(cards, html):
    for card in cards:
        card_img = lxml.html.Element('img')
        card_img.attrib.update({'src':S.tablecardimgs[card-1]})
        card_id = "card-%s" % (card)
        thiscard = html.get_element_by_id(card_id)
        thiscard.append(card_img)
    return html

def add_playercards(seats, html):
    for seat in seats:
        seat_id = "seat-%s" % (seat)
        card1_id = "seat%scard1" % (seat)
        card2_id = "seat%scard2" % (seat)
        card1 = lxml.html.Element('div')
        card1.attrib.update({'id':card1_id, 'class':'faceup card1'})
        card2 = lxml.html.Element('div')
        card2.attrib.update({'id':card2_id, 'class':'faceup card2'})
        thisseat = html.get_element_by_id(seat_id)
        thisseat.append(card1)
        thisseat.append(card2)
    return html

def show_playercards(seats, html):
    for seat in seats:
        remove_facedown(seat, html)
        card_img = lxml.html.Element('img')
        card_img.attrib.update({'src':S.facecardimg})
        card_img2 = lxml.html.Element('img')
        card_img2.attrib.update({'src':S.facecardimg})
        card1_id = "seat%scard1" % (seat)
        card2_id = "seat%scard2" % (seat)
        thiscard = html.get_element_by_id(card1_id)
        thiscard.append(card_img)
        thiscard2 = html.get_element_by_id(card2_id)
        thiscard2.append(card_img2)
    return html

def add_buttons(buttons, html):
    labels = ['fold', 'check', 'bet']
    pokerroom = html.get_element_by_id('poker-room')
    for button in buttons:
        btn = lxml.html.Element('div')
        btn.attrib.update({'class':'btn', 'id':labels[button]})
        btn.text = labels[button].capitalize()
        pokerroom.append(btn)

def add_static(html, static_html):
    pokerroom = html.get_element_by_id('poker-room')
    new_html = lxml.html.fromstring(static_html)
    for child in new_html.iterchildren():
        pokerroom.append(child)

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

def infobox(html):
    pokerroom = html.get_element_by_id('poker-room')

def add_stack_amounts(html):
    spans = ['stack1span', 'stack2span', 'stack3span', 'stack4span',
             'stack5span', 'stack6span', 'stack7span', 'stack8span',
             'stack9span']
    amounts = S.stack_amounts
    for i in range(len(spans)):
        spanid = spans[i]
        spanamt = amounts[i]
        thisspan = html.get_element_by_id(spanid)
        thisspan.text = spanamt

def add_actions(html):
    action_labels = ['seat1action', 'seat2action', 'seat3action', 'seat4action', 'seat5action', 'seat6action', 'seat7action', 'seat8action', 'seat9action']
    actions = S.actions
    for i in range(len(action_labels)):
        actionid = action_labels[i]
        action = actions[i]
        thisaction = html.get_element_by_id(actionid)
        text = lxml.html.fromstring('<span>%s</span>' % (action))
        thisaction.append(text)

def add_dealer_button(html, seat):
    pokerroom = html.get_element_by_id('poker-room')
    element_id = "seat%sbutton" % (seat)
    dealerbtn = lxml.html.Element('div')
    dealerbtn.attrib.update({'class':'dealerbutton', 'id':element_id})
    dealerbtn.text = "D"
    pokerroom.append(dealerbtn)

def add_dealer_buttons(html):
    these_seats = S.has_button
    for seat in these_seats:
        add_dealer_button(html, seat)
        
seats = range(10)[1:]
tablecards = range(len(S.tablecardimgs)+1)[1:]
buttons = range(3)

html = get_static_html()
add_seats(seats, html)
add_tablecards(tablecards, html)
deal_tablecards(tablecards, html)
add_facedown_cards(seats, html)
deal_facedown(seats, html)
add_status(seats, html)
add_names(seats, S.table_config1['names'], html)
add_amounts(seats, S.table_config1['amounts'], html)
add_playercards(seats, html)
show_playercards(S.table_config1['faceup'], html)
add_static(html, static.autocontrols)
add_buttons(buttons, html)
add_slider(html)
amount_input(html)
add_static(html, static.infobox)
add_stack_amounts(html)
add_actions(html)
add_dealer_buttons(html)
render_html(html)
