var $ = window.$
var console = window.console
var pangea = window.pangea
var WebSocket = window.WebSocket

pangea.Card = function(image, selector, parentobj){
  this.image = image
  this.selector = $(selector)
  this.parentobj = parentobj
  this.parent = $(parentobj.select.seat)
  this.dealimg = pangea.constants.facedown
  this.origin = [110, 365] // top, left
}

pangea.Card.prototype.showCard = function(){
  function showIt(){
    thiscard.image = pangea.deck[thiscard.card]
    var cardElement = $('<img>')
    cardElement.attr('src', thiscard.image)
    thiscard.selector.append(cardElement)
  }
  var thiscard = this
  if ($(this.selector).hasClass('card0')){
    this.card = this.parentobj.playercards[0]
    this.parentobj.playercards[0] = null
    showIt()
  }
  if ($(this.selector).hasClass('card1')){
    this.card = this.parentobj.playercards[1]
    this.parentobj.playercards[1] = null
    showIt()
  }
}

pangea.Card.prototype.deal = function(){
  var dealspeed = 250
  var dealElement = $('<img>')
  dealElement.attr('src', this.dealimg)
  var left = (pangea.constants.root.width()/2) - pangea.constants.dealwidth/2
  dealElement.css({'position':'absolute', 'top':this.origin[0],
                   'left':left, 'width':pangea.constants.dealwidth})
  pangea.constants.root.append(dealElement)
  var thiscard = this
  dealElement.animate(
    {'left':this.parent.css('left'), 'top':this.parent.css('top'),
     'width':this.parent.width()}, dealspeed, "linear",
    function(){
      dealElement.remove()
      var cardElement = $('<img>')
      cardElement.attr('src', thiscard.image)
      thiscard.selector.append(cardElement)
    }
  )
}

pangea.Card.prototype.clearCard = function(){
  this.selector.empty()
}

pangea.Card.prototype.returnCard = function(){
  var dealspeed = 250
  var dealElement = $('<img>')
  dealElement.attr('src', this.dealimg)
  var left = (pangea.constants.root.width()/2) - pangea.constants.dealwidth/2
  dealElement.css({'position':'absolute', 'top':this.parent.css('top'),
                   'left':this.parent.css('left'), 'width':this.parent.width()})
  pangea.constants.root.append(dealElement)
  var thiscard = this
  dealElement.animate(
    {'left':left, 'top':thiscard.origin[0],
     'width':pangea.constants.dealwidth}, dealspeed, "linear",
    function(){
      dealElement.remove()
    }
  )
}


