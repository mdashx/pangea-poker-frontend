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

$('#testCloseWebSocket').click(function(){closeWebSocket()})
$('#testFillSeats').click(function(){fillSeats()})
$('#testClearSeats').click(function(){clearSeats()})

var testseats = [{"stack": 101.95, "name": "albogawx", "seat": 0, "empty":0}]