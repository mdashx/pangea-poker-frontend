var pangea = window.pangea

// function wstest1(){
//   // pangea.ws.send("{'potamount':'345'}")
//   // pangea.ws.send("{}")
//   pangea.ws.send('{"potAmount":400.00}')
// }

function test1(){
  var testmsg = {'test':'fillseats'}
  pangea.sendMessage(JSON.stringify(testmsg))
}

function closeWebSocket(){
  pangea.ws.close()
}

$('#testCloseWebSocket').click(function(){closeWebSocket()})

function clearSeats(){
  var msg = {'test':'clearseats'}
  pangea.sendMessage(JSON.stringify(msg))
}

$('#testClearSeats').click(function(){clearSeats()})

// $('.faceup').addClass('hide')
// $('.facedown').addClass('hide')
$('.dealerbutton').addClass('hide')
$('.stack-label').addClass('hide')
$('.tablecard').addClass('hide')
// $('#gameinfo').addClass('hide')
$('#chatbox').addClass('hide')

pangea.GUI.init()

// pangea.API.seats(test_seats)
// function seatstest(){
//   pangea.ws.send('seats')
// }
// pangea.actions.sit()
// pangea.GUI.tocall()
// pangea.GUI.playerstack()