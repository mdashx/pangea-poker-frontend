/*global thiscard */
var $ = window.$
var console = window.console
var pangea = window.pangea
var WebSocket = window.WebSocket

// I should definitely use inheritance to create the board card
// and player card object prototypes, but since there's only these
// two types of cards, I'm just duplicating some code for simplicity.
// If there was a need for a third card, I'd have a base Card prototype
// to inherit from.

pangea.BoardCard = function(selector){
  this.card = null
  this.image = null
  this.selector = selector
  this.dealimg = pangea.constants.facedown
  this.origin = [110, 365] // top, left
}

pangea.BoardCard.prototype.getCard = function(){
  if (pangea.cards.indexOf(this.card) > -1){
    this.image = pangea.deck[this.card]
    return true
  } else {this.image = null; return false}
}

pangea.BoardCard.prototype.show = function(){
  this.getCard()
  if (this.image != null){
    var cardElement = $('<img>')
    cardElement.attr('src', this.image)
    $(this.selector).append(cardElement)
  }
}

pangea.BoardCard.prototype.clearCard = function(){
  $(this.selector).empty()
  this.card = null
  this.image = null
}

pangea.BoardCard.prototype.showing = function(){
  if ($(this.selector).has('img').length > 0){
    return true
  }
  return false
}

pangea.BoardCard.prototype.deal = function(){
  if (this.showing() == false && this.getCard()){
    var dealspeed = 250
    var dealElement = $('<img>')
    dealElement.attr('src', this.dealimg)
    var left = (pangea.constants.root.width()/2) - pangea.constants.dealwidth/2
    dealElement.css({'position':'absolute', 'top':this.origin[0],
                     'left':left, 'width':pangea.constants.dealwidth})
    pangea.constants.root.append(dealElement)
    var thiscard = this
    dealElement.animate(
      {'left':$(this.selector).css('left'), 'top':$(this.selector).css('top'),
       'width':$(this.selector).width()}, dealspeed, "linear",
      function(){
        dealElement.remove()
        thiscard.show()
      }
    )
  }
}

pangea.BoardCard.prototype.returnCard = function(){
  if (this.showing()){
    var dealspeed = 250
    var dealElement = $('<img>')
    dealElement.attr('src', this.dealimg)
    var left = (pangea.constants.root.width()/2) - pangea.constants.dealwidth/2
    this.clearCard()
    dealElement.css({'position':'absolute',
                     'top':$(this.selector).css('top'),
                     'left':$(this.selector).css('left'),
                     'width':$(this.selector).width()})
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
}
