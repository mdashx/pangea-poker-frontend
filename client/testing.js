var console = window.console
var $ = window.$
var pangea = window.pangea

function closeWebSocket(){
  pangea.ws.close()
  console.log("WebSocket Closed")
}

function fillSeats(){
  var num = $('#numplayers').val()
  var msg = {'test':{'fillseats':Number(num)}}
  pangea.sendMessage(JSON.stringify(msg))
}

function clearSeats(){
  var msg = {'test':{'clearseats':''}}
  pangea.sendMessage(JSON.stringify(msg))
}

function dealCards1(){
  var msg = {'test':{'deal1':''}}
  pangea.sendMessage(JSON.stringify(msg))
}

function returnCards(){
  for (var seat in pangea.seats){
    pangea.seats[seat].returnCards()
  }
}

$('#testCloseWebSocket').click(function(){closeWebSocket()})
$('#testFillSeats').click(function(){fillSeats()})
$('#testClearSeats').click(function(){clearSeats()})
$('#testDeal1').click(function(){dealCards1()})
$('#testReturnCards').click(function(){returnCards()})

var testseats = [{"stack": 101.95, "name": "albogawx", "seat": 0, "empty":0}]