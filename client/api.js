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

pangea.API.deal = function(message){
  function dealer(new_dealer){
    pangea.dealer = new_dealer
    pangea.update()
  }
  function holecards(new_cards){
    for (var seat in pangea.seats){
      pangea.seats[seat].playercards = null
    }
    if (pangea.player.sitting != 0){
      pangea.player.holecards = new_cards
    }
  }
  var handlers = {'holecards':holecards, 'dealer':dealer}
  for (var key in message){
    if (message.hasOwnProperty(key)){
      var handler = handlers[key]
      handler(message[key])
    }
  }
  pangea.gui.dealcards()
}

  // if (action == 'holecards'){
  //   pangea.gui.dealcards()
  // }


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



