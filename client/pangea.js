var $ = window.$
var console = window.console
var pangea = window.pangea
var WebSocket = window.WebSocket

pangea.actions = new Object()
pangea.actions.join = function(seatnum){
  var message = {'action':{'join':seatnum}}
  message = JSON.stringify(message)
  pangea.sendMessage(message)
}

pangea.initcards = function(){
  for (var i=0; i < pangea.seats.length; i++){
    var seat = pangea.seats[i]
    seat.facedown1 = new pangea.Card(pangea.constants.facedown, seat.select.facedown1, seat.select.seat)
    seat.facedown2 = new pangea.Card(pangea.constants.facedown, seat.select.facedown2, seat.select.seat)
    seat.faceup1 = new pangea.Card(undefined, seat.select.faceup1, seat.select.seat)
    seat.faceup2 = new pangea.Card(undefined, seat.select.faceup2, seat.select.seat)
  }
}

pangea.init = function(){
  for (var i=0; i<9; i++){
    var newSeat = new pangea.Seat(i)
    pangea.seats.push(newSeat)
    newSeat.update()
  }
  pangea.initcards()
}

pangea.update = function(){
  for (var seat in pangea.seats){
    pangea.seats[seat].update()
  }
  if (pangea.player.sitting != 0){
    pangea.gui.addPlayerControls()
  }  else {
    pangea.gui.addJoinLabel()
  }
  pangea.gui.updatePotAmount()
  pangea.gui.playerstack()
  pangea.getTableOrder()
}

$('.player-info').hover(
  function(){
    if ($(this).hasClass('can-sit')){
      $(this).css('background-color', '#37FF00')
    }},
  function(){
    if ($(this).hasClass('can-sit')){
    $(this).css('background-color', pangea.constants.emptyseatbg)
    }
  })

pangea.init()
pangea.update()

