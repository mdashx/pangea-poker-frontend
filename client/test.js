var pangea = window.pangea

function wstest1(){
  // pangea.ws.send("{'potamount':'345'}")
  // pangea.ws.send("{}")
  pangea.ws.send('{"potAmount":400.00}')
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
$('#gameinfo').addClass('hide')
$('#chatbox').addClass('hide')

pangea.GUI.init()

function emptyTest(){
  // pangea.GUI.seat2.seatEmpty()
  for (var i=0; i < pangea.GUI.seats.length; i++){
    pangea.GUI.seats[i].seatEmpty()
  }
  // for (var seat in pangea.GUI.seats){
  //   // seat.seatEmpty()
  //   console.log(seat)
  // }
}
