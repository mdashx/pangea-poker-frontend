var pangea = window.pangea

// pangea.playerChips(1, 0, 1, 14)
// pangea.playerChips(1, 1, 2, 5)
// pangea.playerChips(1, 2, 3, 8)
// pangea.playerChips(1, 3, 4, 10)
// pangea.playerChips(1, 4, 5, 3)

function random_stacks(positionnum, potBool){
  var player = positionnum
  var stack_limit = 12
  if (potBool==true){
    stack_limit = 20
  }
  function sortNum(a,b){
    return a - b
  }
  function randChip(){
    var chip = pangea.randomIntFromInterval(0,  chips.length-1)
    var this_chip = chips.splice(chip, 1)[0]
    return this_chip + 1
  }
  var chips = [0,1,2,3,4]
  var quantities = []
  for (var j=0; j<5; j++){
    var quantity = pangea.randomIntFromInterval(0,stack_limit)
    quantities.push(quantity)
  }
  quantities.sort(sortNum)
  quantities.reverse()
  if (potBool==true){
    for (var i=0; i<5; i++){
      pangea.potChips(positionnum, i, randChip(), quantities[i])
    }
  } else {
    for (var i=0; i<5; i++){
      pangea.playerChips(positionnum, i, randChip(), quantities[i])
    }
  }
}

function all_random(){
  for (var i=1; i<10; i++){
    random_stacks(i, false)
  }
}

function random_pot(){
  random_stacks(0, true)
  // random_stacks(1, true)
  // random_stacks(2, true)
}

all_random()
random_pot()

// pangea.potChips(0,0,1,2)


// random_stacks(8)
// random_stacks(9)
// random_stacks(3)
// random_stacks(7)

// pangea.playerChips(2, 0, 1, 10)
// pangea.playerChips(2, 1, 2, 8)
// pangea.playerChips(2, 2, 3, 6)
// pangea.playerChips(2, 3, 4, 7)
// pangea.playerChips(2, 4, 5, 4)

// pangea.playerChips(5, 0, 1, 10)
// pangea.playerChips(5, 1, 2, 6)
// pangea.playerChips(5, 2, 3, 7)
// pangea.playerChips(5, 3, 4, 4)
// pangea.playerChips(5, 4, 5, 10)

// random_stacks(4)
// random_stacks(6)
