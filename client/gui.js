var $ = window.$
var console = window.console
var pangea = window.pangea
var WebSocket = window.WebSocket

pangea.gui = new Object()

pangea.gui.addJoinLabel = function(){
  $('#fold').addClass('hide')
  $('#check').addClass('hide')
  $('#bet').addClass('hide')
  $('#bet_slider').addClass('hide')
  $('#bet-amount').addClass('hide')
  $('#bet-label').addClass('hide')
  $('#autocontrols').addClass('hide')
  if ($('#join-label').length == 0){
    var joinLabel = $('<div id="join-label">Choose a seat to join the table.</div>')
    $('#poker-room').append(joinLabel)
  } else {
    $('#join-label').removeClass('hide')
  }
}

pangea.gui.addPlayerControls = function(){
  $('#join-label').addClass('hide')
  $('#fold').removeClass('hide')
  $('#check').removeClass('hide')
  $('#bet').removeClass('hide')
  $('#bet_slider').removeClass('hide')
  $('#bet-amount').removeClass('hide')
  $('#bet-label').removeClass('hide')
  $('#autocontrols').removeClass('hide')
}

pangea.gui.centerPotAmount = function(){
  var width = $('#pot-amount').outerWidth()
  var center = 400
  $('#pot-amount').css({left:center - (width/2)})
}

pangea.gui.updatePotAmount = function(amount){
  $('#pot-amount').text('Pot: ' + String(amount))
  pangea.gui.centerPotAmount()
}

pangea.gui.tocall = function(){
  var selector = '#tocall'
  if (pangea.table.tocall === undefined){
    $(selector).text('To call: 0')
  } else {
    $(selector).text('To call: ' + pangea.table.tocall)
  }
}

pangea.gui.playerstack = function(){
  var selector = '#player-total'
  if (pangea.player.stack === undefined){
    $(selector).text('Stack: 0')
  } else {
    $(selector).text('Stack: ' + pangea.player.stack)
  }
}

