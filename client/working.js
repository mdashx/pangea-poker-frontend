// So Emacs doesn't yell at me for undeclared variables
var $ = window.$
var console = window.console
var pangea = window.pangea
var WebSocket = window.WebSocket

pangea.wsURI = 'ws://localhost:9000'

pangea.API = new Object()

pangea.API.seats = function(seatArray){
  for (var i=0; i < seatArray.length; i++){
    if (seatArray[i].name != undefined) {
      pangea.GUI.updateSeat(seatArray[i])
    }
  }
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
}

pangea.table = function(tocall){
  this.tocall = tocall
}

pangea.API.player = function(message){
  pangea.player.seat = message.seat
  pangea.player.stack = message.stack
  pangea.GUI.update()
}