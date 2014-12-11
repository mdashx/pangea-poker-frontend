var $ = window.$
var console = window.console
var pangea = window.pangea
var WebSocket = window.WebSocket

pangea.API = new Object()

pangea.API.seats = function(seatArray){
  for (var i=0; i < seatArray.length; i++){
    var seatIndex = seatArray[i]['seat']
    pangea.seats[seatIndex].update(seatArray[i])
  }
  pangea.update()
}

pangea.API.player = function(playerArray){
  for (var param in playerArray){
    if (pangea.player.hasOwnProperty(param)){
      pangea.player[param] = playerArray[param]
    } else {
      console.log("Property not found ", param)
    }
  }
  pangea.update()
}

pangea.API.game = function(gameArray){
  for (var param in gameArray){
    if (pangea.game.hasOwnProperty(param)){
      pangea.game[param] = gameArray[param]
    } else {
      console.log("Property not found ", param)
    }
  }
}

pangea.API.deal = function(action){
  if (action == 'holecards'){
    pangea.gui.dealcards()
  }
}

pangea.API.action = function(actionArray){
  var handlers = {'deal':pangea.API.deal}
  for (var action in actionArray){
    if (actionArray.hasOwnProperty(action)){
      var handler = handlers[action]
      console.log(actionArray[action])
      handler(actionArray[action])
    }
  }
}


