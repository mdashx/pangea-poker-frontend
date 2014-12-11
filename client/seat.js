var $ = window.$
var console = window.console
var pangea = window.pangea
var WebSocket = window.WebSocket

pangea.Seat = function(seat, avatar, name, stack){
  this.seat = seat
  this.bg = pangea.constants.seatbg
  if (avatar === undefined) {this.avatar = './images/avatar-default.png'}
  else {this.avatar = avatar}
  this.name = name
  this.stack = stack
  this.action = ''
  this.playing = 0
  this.player = 0
  this.empty = 1
  this.setSelectors()
  this.updateCSS()
  this.sitdown()
}

pangea.Seat.prototype.setSelectors = function(){
  this.select = {}
  this.select.seat = '#seat-' + String(this.seat)
  this.select.status = '#seat-' + String(this.seat) + ' > .player-status'
  this.select.action = '#seat' + String(this.seat) + 'action'
  this.select.name = this.select.status + " > .player-name"
  this.select.stack = this.select.status + " > .player-amount"
  this.select.facedown1 = this.select.seat + " > .down0"
  this.select.facedown2 = this.select.seat + " > .down1"
  this.select.faceup1 = this.select.seat + " > .card0"
  this.select.faceup2 = this.select.seat + " > .card1"
  this.select.button = '#seat' + String(this.seat) + 'button'
}

pangea.Seat.prototype.emptycss = function(){
  $(this.select.seat).addClass('empty-seat')
  $(this.select.seat).addClass('can-sit')
  $(this.select.status).addClass('hide')
  $(this.select.action).text('')
  $(this.select.seat).css('background', pangea.constants.emptyseatbg)
  $(this.select.seat).css('opacity', '0.5')
  $(this.select.seat).css('background-image', 'none')
  $(this.select.seat).css('border-color', pangea.constants.emptyseatbg)
  if (pangea.player.sitting != 0){
    $(this.select.seat).removeClass('can-sit')
  }
}

pangea.Seat.prototype.occupiedcss = function(){
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

pangea.Seat.prototype.onTheButton = function(){
  if (this.seat == pangea.dealer){
    $(this.select.button).removeClass('hide')
  } else {
    $(this.select.button).addClass('hide')
  }
}

pangea.Seat.prototype.updateCSS = function(){
  if (this.empty == 1){this.emptycss()}
  else {this.occupiedcss()}
}

pangea.Seat.prototype.sitdown = function(){
  $(this.select.seat).unbind('click')
  if (pangea.player.sitting == 0){
    $(this.select.seat).click(function(){
      var seatnum = Number(this.id.split('-')[1])
      pangea.actions.join(seatnum)
    })
  } 
}

pangea.Seat.prototype.holdingCards = function(){
  var theseCards = [this.faceup1, this.faceup2,
                    this.facedown1, this.facedown2]
  for (var i=0; i < theseCards.length; i++){
    var hasImage = theseCards[i].selector
    if (theseCards[i].selector.has('img').length > 0){
      return true
    }
  }
  return false
}

pangea.Seat.prototype.returnCards = function(){
  if (this.holdingCards()){
    this.faceup1.clearCard()
    this.faceup2.clearCard()
    this.facedown1.clearCard()
    this.facedown2.clearCard()
    this.facedown1.returnCard()
    this.facedown2.returnCard()    
  }
}

pangea.Seat.prototype.update = function(params){
  for (var param in params){
    if (this.hasOwnProperty(param)){
      this[param] = params[param]
    } else {
      console.log("Parameter not found ", param)
    }
  }
  if (this.seat === pangea.player.seat){
    this.player = 1
  } else { this.player = 0}
  this.updateCSS()
  this.sitdown()
  this.onTheButton()
}
