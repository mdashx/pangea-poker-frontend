var $ = window.$
var console = window.console
var pangea = window.pangea
var WebSocket = window.WebSocket

pangea.game = new Object()
pangea.game.pot = [0]
pangea.game.tocall = 0
pangea.seats = []

pangea.Player = function(seat, stack){
  this.seat = seat
  this.stack = stack
  this.holecards = []
  this.sitting = 0
}

pangea.player = new pangea.Player(null, 0)

