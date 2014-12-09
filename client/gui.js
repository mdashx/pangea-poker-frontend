var $ = window.$
var console = window.console
var pangea = window.pangea

pangea.constants = {}
pangea.constants.emptyseatbg = '#3C3D3D'
pangea.constants.seatbg = '#616f91'
pangea.constants.seatborder = '#CAC7FF'


pangea.GUI = new Object()

pangea.GUI.Seat = function(seat, avatar, name, stack){
  this.seat = seat
  this.bg = pangea.constants.seatbg
  if (avatar === undefined) {this.avatar = './images/avatar-default.png'}
  else {this.avatar = avatar}
  this.name = name
  this.stack = stack
  this.action = ''
  this.setSelectors()
}

pangea.GUI.Seat.prototype.setSelectors = function(){
  this.select = {}
  this.select.seat = '#seat-' + String(this.seat)
  this.select.status = '#seat-' + String(this.seat) + ' > .player-status'
  this.select.action = '#seat' + String(this.seat) + 'action'
  this.select.name = this.select.status + " > .player-name"
  this.select.stack = this.select.status + " > .player-amount"
}

pangea.GUI.Seat.prototype.seatEmpty = function(){
  $(this.select.seat).removeClass('player-info')
  $(this.select.seat).addClass('empty-seat')
  $(this.select.seat).addClass('can-sit')
  $(this.select.status).addClass('hide')
  $(this.select.action).text('')
}

pangea.GUI.Seat.prototype.update = function(){
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

pangea.GUI.updateSeat = function(params){
  var thisSeat = pangea.GUI.seats[params['seat']]
  for (var param in params){
    if (thisSeat.hasOwnProperty(param)){
      thisSeat[param] = params[param]
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
    var newSeat = new pangea.GUI.Seat(i+1)
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
  pangea.actions.sit()
}