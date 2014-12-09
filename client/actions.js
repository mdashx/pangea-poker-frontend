var $ = window.$
var console = window.console
var pangea = window.pangea
var WebSocket = window.WebSocket

pangea.actions = new Object()

pangea.actions.join = function(seatnum){
  var message = {'action':{'join':seatnum}}
  message = JSON.stringify(message)
  pangea.sendMessage(message)
}

pangea.actions.sit = function(){
  // if (pangea.player.seat != undefined){
  //   $('.empty-seat').click(function(){
  //     console.log('not empty')
  //     console.log(pangea.player.seat == undefined)
  //     return true
  //   })
  // } else {
  //   $('.empty-seat').click(function(){
  //     var seatnum = Number(this.id.split('-')[1]) - 1
  //     console.log(pangea.player.seat)
  //     console.log(pangea.player.seat === undefined)
  //     pangea.actions.join(seatnum)
  //   })}

  if (pangea.player.seat == undefined){
    $('.empty-seat').click(function(){
      var seatnum = Number(this.id.split('-')[1]) - 1
      console.log(pangea.player.seat)
      console.log(pangea.player.seat === undefined)
      pangea.actions.join(seatnum)
    })
  } else {
    $('.empty-seat').unbind('click')
  }
}