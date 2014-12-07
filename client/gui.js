var $ = window.$
var console = window.console
var pangea = window.pangea

pangea.constants = {}
pangea.constants.emptyseatbg = '#3C3D3D'

pangea.GUI = new Object()

pangea.GUI.Seat = function(seat, avatar, name, stack){
  this.seat = seat
  if (avatar === undefined) {this.avatar = './images/avatar-default.png'}
  else {this.avatar = avatar}
  this.name = name
  this.stack = stack
  this.setSelectors()
}

pangea.GUI.Seat.prototype.setSelectors = function(){
  this.select = {}
  this.select.seat = '#seat-' + String(this.seat)
  this.select.status = '#seat-' + String(this.seat) + ' > .player-status'
  this.select.action = '#seat' + String(this.seat) + 'action'
}

pangea.GUI.Seat.prototype.seatEmpty = function(){
  this.avatar = null
  this.name = null
  this.stack = null
  this.action = ''
  this.update()
}

pangea.GUI.Seat.prototype.update = function(){
  if (this.avatar === null){
    $(this.select.seat).css('background-image', 'none')
    $(this.select.seat).css('background', pangea.constants.emptyseatbg)
    $(this.select.seat).css('opacity', '.5')
    $(this.select.seat).css('border-color', pangea.constants.emptyseatbg)
  } else {
    $(this.select.seat).css('background-image', 'url(' + this.avatar + ')')
  }
  if (this.name === null || this.stack === null){
    $(this.select.status).addClass('hide')
  }
  $(this.select.action).text(this.action)
}

pangea.GUI.seats = []

pangea.GUI.init = function(){
  for (var i=0; i<9; i++){
    var newSeat = new pangea.GUI.Seat(i+1)
    pangea.GUI.seats.push(newSeat)
  }
  for (var j=0; j < pangea.GUI.seats.length; j++){
    pangea.GUI.seats[j].seatEmpty()
  }
  pangea.GUI.updatePotAmount(0)
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
