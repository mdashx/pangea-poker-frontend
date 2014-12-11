var $ = window.$
var console = window.console
var WebSocket = window.WebSocket

var pangea = new Object()
pangea.pokerRoom = document.getElementById('poker-room')

pangea.randomIntFromInterval = function(min,max)
{
    return Math.floor(Math.random()*(max-min+1)+min);
}

pangea.dealerTray = function(){
  function addDealerChip(row){
    var rows = ['edge-1', 'edge-2', 'edge-3', 'edge-4', 'edge-5']
    var baseTop = 65
    var pokerRoom = document.getElementById('poker-room')
    var chipDiv = document.createElement('div')
    chipDiv.className = 'chip-edge ' + rows[row]
    var thistop = baseTop + (3 * dealerchips[row])
    chipDiv.style.top = String(thistop) + 'px'
    var chipSpot = document.createElement('div')
    chipSpot.className = 'chip-spot'
    chipSpot.style.left = String(pangea.randomIntFromInterval(2,8))
                        + 'px'
    chipDiv.appendChild(chipSpot)
    pokerRoom.appendChild(chipDiv)
    dealerchips[row] += 1
    return chipDiv
  }

  function addChips(row, quantity){
    for (var i=0; i<quantity; i++){
      addDealerChip(row)
    }
  }

  var dealerchips = [0, 0, 0, 0, 0]
  for (var i=0; i<5; i++){
    addChips(i, pangea.randomIntFromInterval(5,14))
  }
}

pangea.addChip = function(chipnum, left, top, potBool){
  var chipDiv = document.createElement('div')
  if (potBool==true){
    chipDiv.className = 'chip potchip chip' + chipnum
  } else {
    chipDiv.className = 'chip chip' + chipnum
  }
  chipDiv.style.top = String(top) + 'px'
  chipDiv.style.left = String(left) + 'px'
  pangea.pokerRoom.appendChild(chipDiv)
}

pangea.playerChips = function(playernum, stacknum, chipnum, quantity){
  var p1 = [[494, 90], [475, 92], [488, 106], [507, 104], [470, 108]]
  var p2 = [[644, 132], [630, 142], [648, 149], [631, 160], [647, 167]]
  var p3 = [[644, 257], [630, 267], [648, 274], [631, 285], [647, 292]]
  var p4 = [[582, 333], [565, 328], [599, 328], [549, 333], [616, 333]]
  var p5 = [[395, 345], [378, 340], [412, 340], [362, 345], [429, 345]]
  var p6 = [[208, 333], [191, 328], [225, 328], [175, 333], [242, 333]]
  var p7 = [[145, 257], [159, 267], [141, 274], [158, 285], [142, 292]]
  var p8 = [[145, 132], [159, 142], [141, 149], [158, 160], [142, 167]]
  var p9 = [[291, 90], [310, 92], [297, 106], [278, 104], [315, 108]]
  var players = Array(p1, p2, p3, p4, p5, p6, p7, p8, p9)
  var player = players[playernum-1]
  var pokerRoom = document.getElementById('poker-room')
  var bottom_chip = player[stacknum]
  for (var i=0; i<quantity; i++){
    var top = bottom_chip[1] - (2 * i)
    pangea.addChip(chipnum, bottom_chip[0], top, false)
  }
}

pangea.potChips = function(potnum, stacknum, chipnum, quantity){
  var pot1 = [[390, 280], [372, 280], [408, 280], [354, 280], [426, 280]]
  var pot2 = [[277, 280], [259, 280], [295, 280], [241, 280], [313, 280]]
  var pot3 = [[508, 280], [490, 280], [526, 280], [472, 280], [544, 280]]
  var pots = Array(pot1, pot2, pot3)
  var pot = pots[potnum]

  var bottom_chip = pot[stacknum]
  for (var i=0; i<quantity; i++){
    var top = bottom_chip[1] - (2 * i)
    pangea.addChip(chipnum, bottom_chip[0], top, true)
  }
}

pangea.hideBetLabels = function(){
  var elements = document.getElementsByClassName('stack-label')
    for(var i=0; i < elements.length; i++){
      if (elements[i].textContent == ''){
        elements[i].className = 'stack-label hide'
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

pangea.onMessage = function(message){
  var handlers = {'action':pangea.API.action, 'game':pangea.API.game, 'seats':pangea.API.seats, 'player':pangea.API.player}
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

pangea.dealerTray()
pangea.hideBetLabels()
pangea.wsURI = 'ws://localhost:9000'
pangea.ws = pangea.openWebSocket()