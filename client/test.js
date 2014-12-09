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

// function bgtest(){
//   pangea.GUI.seat1.avatar = './images/avatar-default2.png'
//   pangea.GUI.seat1.update()
// }

$('.faceup').addClass('hide')
$('.facedown').addClass('hide')
$('.dealerbutton').addClass('hide')
$('.stack-label').addClass('hide')
$('.tablecard').addClass('hide')
// $('#gameinfo').addClass('hide')
$('#chatbox').addClass('hide')

pangea.GUI.init()

// pangea.API.seats(test_seats)

function seatstest(){
  pangea.ws.send('seats')
}

// pangea.actions.sit()

// pangea.GUI.tocall()
// pangea.GUI.playerstack()