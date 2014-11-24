import lxml.html
import settings as S

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
    def add_seat(seat, pokerroom):
        seat_id = "seat-%s" % (seat)
        thisseat = lxml.html.Element('div')
        thisseat.attrib.update({'class':'player-info', 'id':seat_id})
        pokerroom.append(thisseat)
        return pokerroom
    pokerroom = html.get_element_by_id('poker-room')
    for seat in seats:
        pokerroom = add_seat(seat, pokerroom)
    return html

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

seats = range(10)[1:]
tablecards = range(6)[1:]
        
html = get_static_html()
html = add_seats(seats, html)
html = add_tablecards(tablecards, html)
html = deal_tablecards(tablecards, html)
html = add_playercards(seats, html)
html = show_playercards(seats, html)
render_html(html)
