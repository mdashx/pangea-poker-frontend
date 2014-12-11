var $ = window.$
var console = window.console
var pangea = window.pangea

pangea.constants = {}
pangea.constants.root = $('#poker-room')
pangea.constants.emptyseatbg = '#3C3D3D'
pangea.constants.seatbg = '#616f91'
pangea.constants.seatborder = '#CAC7FF'
pangea.constants.facedown = './images/cards/Red_Back-150.png'
pangea.constants.dealwidth = 30

pangea.GUI = new Object()

pangea.GUI.Seat = function(seat, avatar, name, stack){
  this.seat = seat
  this.bg = pangea.constants.seatbg
  if (avatar === undefined) {this.avatar = './images/avatar-default.png'}
  else {this.avatar = avatar}
  this.name = name
  this.stack = stack
  this.action = ''
  this.playing = undefined
  this.seat.player = false
  this.setSelectors()
  this.empty = 1
}

pangea.GUI.Seat.prototype.setSelectors = function(){
  this.select = {}
  this.select.seat = '#seat-' + String(this.seat + 1)
  this.select.status = '#seat-' + String(this.seat + 1) + ' > .player-status'
  this.select.action = '#seat' + String(this.seat + 1) + 'action'
  this.select.name = this.select.status + " > .player-name"
  this.select.stack = this.select.status + " > .player-amount"
  this.select.facedown1 = this.select.seat + " > .down1"
  this.select.facedown2 = this.select.seat + " > .down2"
  this.select.faceup1 = this.select.seat + " > .card1"
  this.select.faceup2 = this.select.seat + " > .card2"
}

pangea.GUI.Seat.prototype.seatEmpty = function(){
  $(this.select.seat).removeClass('player-info')
  $(this.select.seat).addClass('empty-seat')
  $(this.select.seat).addClass('can-sit')
  $(this.select.status).addClass('hide')
  $(this.select.action).text('')
  $(this.select.seat).css('background', pangea.constants.emptyseatbg)
  $(this.select.seat).css('opacity', '0.5')
  $(this.select.seat).css('background-image', 'none')
  $(this.select.seat).css('border-color', pangea.constants.emptyseatbgdd)
  this.seat.playing = false
}

pangea.GUI.Seat.prototype.update = function(){
  if (this.empty == 1){
    console.log('empty')
    this.seatEmpty()
  } else {
    console.log('not empty')
    $(this.select.seat).removeClass('empty-seat')
    $(this.select.seat).removeClass('can-sit')
    $(this.select.seat).addClass('player-info')
    $(this.select.seat).css('background', this.bg)
    $(this.select.seat).css('opacity', '1')
    $(this.select.seat).css('background-image', 'url(' + this.avatar + ')')
    $(this.select.action).html(this.action)
    $(this.select.status).removeClass('hide')
    $(this.select.name).text(this.name)
    $(this.select.stack).text(this.stack)
    $(this.select.seat).css('border-color', pangea.constants.seatborder)
  }
}

pangea.GUI.updateSeat = function(params){
  var thisSeat = pangea.GUI.seats[params['seat']]
  for (var param in params){
    if (thisSeat.hasOwnProperty(param)){
      thisSeat[param] = params[param]
      // this.playing = true
    }
  }
  thisSeat.update()
}

pangea.GUI.centerPotAmount = function(){
  var width = $('#pot-amount').outerWidth()
  var center = 400
  $('#pot-amount').css({left:center - (width/2)})
}

pangea.GUI.updatePotAmount = function(amount){
  $('#pot-amount').text('Pot: ' + String(amount))
  pangea.GUI.centerPotAmount()
}

pangea.GUI.tocall = function(){
  var selector = '#tocall'
  if (pangea.table.tocall === undefined){
    $(selector).text('To call: 0')
  } else {
    $(selector).text('To call: ' + pangea.table.tocall)
  }
}

pangea.GUI.playerstack = function(){
  var selector = '#player-total'
  if (pangea.player.stack === undefined){
    $(selector).text('Stack: 0')
  } else {
    $(selector).text('Stack: ' + pangea.player.stack)
  }
}

pangea.GUI.controls = function(){
  if (pangea.player.seat == undefined){
    $('#fold').addClass('hide')
    $('#check').addClass('hide')
    $('#bet').addClass('hide')
    $('#autocontrols').addClass('hide')
    $('#bet_slider').addClass('hide')
    $('#bet-amount').addClass('hide')
    $('#bet-label').addClass('hide')
    $('#join-label').removeClass('hide')
  } else {
    $('#fold').removeClass('hide')
    $('#check').removeClass('hide')
    $('#bet').removeClass('hide')
    $('#autocontrols').removeClass('hide')
    $('#bet_slider').removeClass('hide')
    $('#bet-amount').removeClass('hide')
    $('#bet-label').removeClass('hide')
    $('#join-label').addClass('hide')
  }
}

pangea.GUI.playerSeated = function(){
  if (pangea.player.seat != undefined){
    $('*').removeClass('can-sit')
  }
}

pangea.GUI.seats = []

pangea.GUI.init = function(){
  for (var i=0; i<9; i++){
    var newSeat = new pangea.GUI.Seat(i)
    pangea.GUI.seats.push(newSeat)
  }
  for (var j=0; j < pangea.GUI.seats.length; j++){
    pangea.GUI.seats[j].seatEmpty()
  }
  pangea.GUI.update()
}

pangea.GUI.update = function(){
  pangea.GUI.updatePotAmount(0)
  pangea.GUI.tocall()
  pangea.GUI.playerstack()
  pangea.GUI.controls()
  pangea.GUI.playerSeated()
  pangea.GUI.initcards()
  pangea.actions.sit()
  pangea.findPlayerSeat()
}

pangea.GUI.Card = function(image, selector, parentSelector){
  this.image = image
  this.selector = $(selector)
  this.parent = $(parentSelector)
  this.dealimg = pangea.constants.facedown
  this.origin = [110, 365] // top, left
}

pangea.GUI.Card.prototype.deal = function(){
  var dealspeed = 250
  var dealElement = $('<img>')
  dealElement.attr('src', this.dealimg)
  var left = (pangea.constants.root.width()/2) - pangea.constants.dealwidth/2
  dealElement.css({'position':'absolute', 'top':this.origin[0],
                   'left':left, 'width':pangea.constants.dealwidth})
  pangea.constants.root.append(dealElement)
  var thiscard = this
  dealElement.animate(
    {'left':this.parent.css('left'), 'top':this.parent.css('top'),
     'width':this.parent.width()}, dealspeed, "linear",
    function(){
      dealElement.remove()
      var cardElement = $('<img>')
      cardElement.attr('src', thiscard.image)
      thiscard.selector.append(cardElement)
    }
  )
}

pangea.GUI.initcards = function(){
  for (var i=0; i < pangea.GUI.seats.length; i++){
    var seat = pangea.GUI.seats[i]
    seat.facedown1 = new pangea.GUI.Card(pangea.constants.facedown, seat.select.facedown1, seat.select.seat)
    seat.facedown2 = new pangea.GUI.Card(pangea.constants.facedown, seat.select.facedown2, seat.select.seat)
    seat.faceup1 = new pangea.GUI.Card(undefined, seat.select.faceup1, seat.select.seat)
    seat.faceup2 = new pangea.GUI.Card(undefined, seat.select.faceup2, seat.select.seat)
  }
}

pangea.GUI.dealcards = function(){
  var delay = 50
  var dealTheseCards = []
  for (var i=0; i < pangea.GUI.seats.length; i++){
    var seat = pangea.GUI.seats[i]
    if (seat.playing == true){
      if (seat.player == true){
        seat.faceup1.image = pangea.deck[pangea.player.holecards[0]]
        dealTheseCards.push(seat.faceup1)
      } else {dealTheseCards.push(seat.facedown1)}
    }
  }
  for (var j=0; j < pangea.GUI.seats.length; j++){
    var seat = pangea.GUI.seats[j]
    if (seat.playing == true){
      if (seat.player == true){
        seat.faceup2.image = pangea.deck[pangea.player.holecards[1]]
        dealTheseCards.push(seat.faceup2)
      } else {dealTheseCards.push(seat.facedown2)}
    }
  }
  for (var k=0; k < dealTheseCards.length; k++){
    window.setTimeout(function(){
      var thiscard = dealTheseCards.shift()
      thiscard.deal()
    }, delay * k)
  }
}

// var testcard1 = new pangea.GUI.Card(pangea.constants.facedown, '#seat-3 > .down1', '#seat-3')
// var testcard2 = new pangea.GUI.Card(pangea.constants.facedown, '#seat-4 > .down1', '#seat-4')
// var testcard3 = new pangea.GUI.Card(pangea.constants.facedown, '#seat-3 > .down2', '#seat-3')
// var testcard4 = new pangea.GUI.Card(pangea.constants.facedown, '#seat-4 > .down2', '#seat-4')

// window.setTimeout(function(){testcard1.deal()}, 0);
// window.setTimeout(function(){testcard2.deal()}, 200);
// window.setTimeout(function(){testcard3.deal()}, 800);
// window.setTimeout(function(){testcard4.deal()}, 1000);