// So Emacs doesn't yell at me for undeclared variables
var $ = window.$
var console = window.console
var pangea = window.pangea
var WebSocket = window.WebSocket

pangea.wsURI = 'ws://localhost:9000'

function centerPotAmount(){
  var width = $('#pot-amount').outerWidth()
  var center = 400
  $('#pot-amount').css({left:center - (width/2)})
}

function updatePotAmount(amount){
  $('#pot-amount').text('Pot: ' + String(amount))
  centerPotAmount()
}

pangea.API = new Object()

pangea.API.potAmount = function(message){
  // should make this take an ordered list of pots
  updatePotAmount(message)
  centerPotAmount()
}

pangea.onMessage = function(message){
  var handlers = {'potAmount':pangea.API.potAmount}
  message = JSON.parse(message)
  for (var key in message){
    if (message.hasOwnProperty(key)){
      var handler = handlers[key]
      handler(message[key])
    }
  }
}

pangea.openWebSocket = function(){
  var ws  = new WebSocket(pangea.wsURI)
  ws.onmessage = function(event){
    pangea.onMessage(event.data)
  }
  return ws
}

pangea.ws = pangea.openWebSocket()
centerPotAmount()


