var $ = window.$
var console = window.console

// a = $('#pot-amount')
// [<div id=​"pot-amount">​Pot: 303.00​</div>​]
// a
// [<div id=​"pot-amount">​Pot: 303.00​</div>​]
// a.text
// jquery.min.js:3 function (a){return V(this,function(a){return void 0===a?m.text(this):this.empty().append((this[0]&&this[0].ownerDocument||y).createTextNode(a))},null,a,arguments.length)}
// a.text()
// "Pot: 303.00"
// a.text('Pot: 100.00')
// [<div id=​"pot-amount">​Pot: 100.00​</div>​]
// a.width()
// 120
// a.left()
// VM323:2 Uncaught TypeError: undefined is not a function
// a.left
// undefined
// a.css('left')
// "340px"
// a.css('top')
// "20px"

// $('#pot-amount').css({left:200px})

function centerPotAmount(){
  var width = $('#pot-amount').outerWidth()
  var center = 400
  $('#pot-amount').css({left:center - (width/2)})
}

function updatePotAmount(amount){
  $('#pot-amount').text('Pot: ' + String(amount))
}

centerPotAmount()