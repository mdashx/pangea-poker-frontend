var pangea = window.pangea

pangea.makedeck = new Object()
pangea.makedeck.symbols = []

pangea.makedeck.makesymbols = function(){
  var ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
  var suits = ['C', 'D', 'H', 'S']
  for (var i=0; i < suits.length; i++){
    for (var j=0; j < ranks.length; j++){
      pangea.makedeck.symbols.push(ranks[j] + suits[i])
    }
  }
}

pangea.makedeck.makesymbols()

pangea.deck1 = {}
pangea.deck2 = {}

pangea.makedeck.deck1 = function(){
  var prefix = './images/cards/'
  var suffix = '-150.png'
  for (var i=0; i < pangea.makedeck.symbols.length; i++){
    var filename = prefix + pangea.makedeck.symbols[i] + suffix
    pangea.deck1[pangea.makedeck.symbols[i]] = filename
  }
}

pangea.makedeck.deck2 = function(){
  var prefix = './images/4color/'
  var suffix = '-150.png'
  for (var i=0; i < pangea.makedeck.symbols.length; i++){
    var filename = prefix + pangea.makedeck.symbols[i] + suffix
    pangea.deck2[pangea.makedeck.symbols[i]] = filename
  }
}

pangea.makedeck.deck1()
pangea.makedeck.deck2()

pangea.deck = pangea.deck1
