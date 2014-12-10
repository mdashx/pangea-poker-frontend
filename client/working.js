// So Emacs doesn't yell at me for undeclared variables
var $ = window.$
var console = window.console
var pangea = window.pangea
var WebSocket = window.WebSocket

pangea.wsURI = 'ws://localhost:9000'

pangea.API = new Object()

pangea.API.seats = function(seatArray){
  for (var i=0; i < seatArray.length; i++){
      pangea.GUI.updateSeat(seatArray[i])
  }
}

pangea.tmpholecards = function(){
  pangea.player.holecards = ['AS', 'AD']
}

pangea.onMessage = function(message){
  var handlers = {'potAmount':pangea.API.potAmount, 'seats':pangea.API.seats, 'player':pangea.API.player}
  message = JSON.parse(message)
  console.log('Recieved: ', message)
  for (var key in message){
    if (message.hasOwnProperty(key)){
      var handler = handlers[key]
      handler(message[key])
    }
  }
}

pangea.sendMessage = function(message){
  pangea.ws.send(message)
  console.log('Sent: ', message)
}

pangea.openWebSocket = function(){
  var ws  = new WebSocket(pangea.wsURI)
  ws.onmessage = function(event){
    pangea.onMessage(event.data)
  }
  return ws
}

pangea.ws = pangea.openWebSocket()

pangea.player = function(seat, stack){
  this.seat = seat
  this.stack = stack
  this.holecards = undefined
  this.player = false
}

pangea.table = function(tocall){
  this.tocall = tocall
  this.activeSeats = []
}

pangea.findPlayerSeat = function(){
  for (var i=0; i<pangea.GUI.seats.length; i++){
    if (pangea.GUI.seats[i].seat == pangea.player.seat){
      pangea.GUI.seats[i].player = true
    } else {
      pangea.GUI.seats[i].player = false
    }
  }
}

pangea.API.player = function(message){
  pangea.player.seat = message.seat
  pangea.player.stack = message.stack
  pangea.player.holecards = undefined
  pangea.findPlayerSeat()
  pangea.GUI.update()
  pangea.tmpholecards()
}

