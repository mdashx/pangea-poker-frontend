var $ = window.$
var console = window.console
var pangea = window.pangea
var WebSocket = window.WebSocket

pangea.game = new Object()
pangea.game.pot = [0]
pangea.game.tocall = 0
pangea.seats = []
pangea.dealer = undefined
pangea.tableOrder = [0,1,2,3,4,5,6,7,8]
pangea.cards = []

for (var card in pangea.deck){
  if (pangea.deck.hasOwnProperty(card)){
    pangea.cards.push(card)
  }
}

pangea.getTableOrder = function(){
  pangea.tableOrder = []
  var start = pangea.dealer + 1 // start with position after the dealer
  for (var i=start; i<start + pangea.seats.length; i++){
    var seatnum = i
    if (seatnum > pangea.seats.length - 1){seatnum = seatnum - pangea.seats.length}
    pangea.tableOrder.push(seatnum)
  }
}

pangea.Player = function(seat, stack){
  this.seat = seat
  this.stack = stack
  this.holecards = []
  this.sitting = 0
}

pangea.player = new pangea.Player(null, 0)

