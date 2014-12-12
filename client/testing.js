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
  pangea.gui.returnCards()
}

function showCards(){
  var msg = {'test':{'showcards':''}}
  pangea.sendMessage(JSON.stringify(msg))
}

function deal2(){
  var msg = {'test':{'deal2':''}}
  pangea.sendMessage(JSON.stringify(msg))
}
function deal3(){
  var msg = {'test':{'deal3':''}}
  pangea.sendMessage(JSON.stringify(msg))
}
function deal4(){
  var msg = {'test':{'deal4':''}}
  pangea.sendMessage(JSON.stringify(msg))
}

$('#testCloseWebSocket').click(function(){closeWebSocket()})
$('#testFillSeats').click(function(){fillSeats()})
$('#testClearSeats').click(function(){clearSeats()})
$('#testDeal1').click(function(){dealCards1()})
$('#testReturnCards').click(function(){returnCards()})
$('#testShowCards').click(function(){showCards()})
$('#testDeal2').click(function(){deal2()})
$('#testDeal3').click(function(){deal3()})
$('#testDeal4').click(function(){deal4()})

var testseats = [{"stack": 101.95, "name": "albogawx", "seat": 0, "empty":0}]

var testboard = {'board':{0:'AH',1:'AS', 2:'AD'}}

function goboard(){
  pangea.API.deal(testboard)
}