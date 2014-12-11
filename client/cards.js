var $ = window.$
var console = window.console
var pangea = window.pangea
var WebSocket = window.WebSocket

pangea.Card = function(image, selector, parentSelector){
  this.image = image
  this.selector = $(selector)
  this.parent = $(parentSelector)
  this.dealimg = pangea.constants.facedown
  this.origin = [110, 365] // top, left
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

