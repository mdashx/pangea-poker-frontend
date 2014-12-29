Okay, I'm trying to place the seats at the poker table, and I'm writing a script to calculate points and write out CSS, so I can easily change things, if for instance the center point of the table or nnsize of the table image changes, or if we need more or less seats, etc.
Trying to place the seats by putting in the x,y coordinates for each seat manually is a pain in the ass.

So from the equation of an ellipse, I've got:

x = ab / square_root of b**2 + a**2(tan theta)**2

y = ab / square_root of a**2 + (b**2 / (tan theta)**2

courtesy: http://math.stackexchange.com/questions/22064/calculating-a-point-that-lies-on-an-ellipse-given-an-angle

a is the horizontal radius
b is the vertical radius

From my SVG file I have:

a = 291.328
b = 168.99852

... I think. Those numbers are labeled rx and ry in the file.

Python:

x = a*b / math.sqrt(b**2 + (a**2 * math.tan(theta)**2))
y = a*b / math.sqrt(a**2 + (b**2 / math.tan(theta)**2))

Cool, I've got the seats laid out in an ellipse, but around the top left corner as zero.

Alright, shifting the coordinates after calculating points on ellipse, so zero is center of table. Everything works perfect for one quadrant, but I can only get points in one quadrant, i.e. 180 deg and 360 are the same point. So, 45, 90 and 180 degrees are spaced out as expected, but I'm missing some positive/negative values or something.

Yep, did some experimenting to make sure. Each quadrant has it's own combination of + - for x and y, so I have to get the code to straighten those out depending on theta.

Got the +/- worked out, now I just need to use a larger ellipse to make a little more room at the table.

Since the seats are position by the top left corner and I'm using rectangles, the right and left sides of the table are not symmetrical, so I'm gonna use some JS to position the left side based on the coordinates on the right side.

Perfect. Now I'm gonna get the JS to write out the top/left CSS for all of the player-info elements. This way we'll have the hardcoded CSS instead of adding extraneous JS code to the client, but the hardcoded CSS is generated programatically, so it can be easily changed.

All good. I think next I will work on showing the flop, turn and river.

## Cards

Gonna try using these first... I bookmarked the project a long time ago and I've been waiting for a chance to use it:

http://donpark.github.io/scalable-css-playing-cards/

Actually, that might be more complicated than I need, since I'm using fixed sizes for now. But I can use the images that the CSS library is based on:

https://code.google.com/p/vectorized-playing-cards/

convert -background none 10C.svg 10C.png
convert 10C.png -trim +repage 10C.png
convert 10C.png -resize 100x 10C.png

Just using those images and converting to the sizes I'll need is good. Gonna write some code to place the cards automatically, so I can easily try different sizes and spacing.

K, I got the Python script calculating the top/left coordinates to place the cards in the center. I'm gonna do the rest of the placement based on spacing between the cards.

Beautiful.

---

Got the player cards placed at the seats programatically. Looking at it now, I think I should use a larger size for the face up player cards. (The facedown ones will be smaller because it will also show the player's avatar.)

I'm also going to start generating the HTML with python, so I can easily add new elements for all of the various positions. (In the finished client this will all be done with JS/AngularJS.)

All good. I was going to add the card image elements with JS, but I'll just do it in Python for now, since the point now is to get the design down, not to make it dynamic.

Hmmm... now that I'm doing all this, I'm not comfortable having to run a Python script and then a JS script and then copy the JS output to create the CSS positions for the seat, so I'm gonna do the mirror image calculations in Python. Then I can just have a build.py that runs everything.

Before I get into that though, gotta find a good size and placement for face up player cards and then write the script to resize and rename all the cards.

---

Eventually for the avatars, I'd like the player to be able to replace specific player's or all players' avatars with the default avatars, in case someone's avatar is offensive or doesn't load. Players could also select to use default avatars by default, and could maybe choose between, pink, blue, black, rainbow, etc. for the default avatars.

## Fri Nov 21 13:31:27 EST 2014

I recreated the table graphics yesterday and added a tray for the dealer chips. The chips get placed in the tray with a JS function that places a random amount of chips and puts the edge spots in different positions. I'm going to keep all of the JS in a global `pangea` object, to avoid namespace collisions.

Now I need to place the avatars/seats on the new table. The code I already have for placing the seats at angles should work fine, but I might need to adjust the code for shifting to a new center, and I need to calculate the mirror images in the Python program, not in JS. I'm going to keep all of the variables in a settings file, to quicly experiment with different sizes, etc. Also, instead of writing a bunch of CSS files, I'm just going to build up a dict of all of the CSS rules and then write them all out at once.

https://shkspr.mobi/blog/2013/03/inkscape-cropping-svg-files-on-the-command-line/
inkscape --verb=FitCanvasToDrawing --verb=FileSave --verb=FileClose *.svg

## Mon Nov 24 09:38:06 EST 2014

checked in the code to render tablecards and faceup cards. Next I'm going to add the status bar and also the player's name.

Status bar/name/amount looks good. Faceup cards are on top of status. Now to make facedown cards underneath status and remove facedown cards before showing faceup cards.

All good, now I need to add the avatars back in and I'll be caught up with where I was with the original table design.

## Tue Nov 25 16:21:05 EST 2014

To Do:
- positions / JS for player chips, dealer button, pot chips, side pot
- action timer
- muck / show cards prompt
- settings window

--- 

Not part of the design:
- get text from chat input
- bet amount slider based on limit / player stack

# Mon Dec  1 09:38:01 EST 2014

Ok, getting back to it after a break for Thanksgiving and a chess tournament. I'm gonna look back at what posted in Slack to see what I need to work on, plus I know I need to write a script to crop, resize, and convert all of the card images. Also I'd like to produce a four-color deck if possible. Oh yea, the settings window.

Pot chips, settings window, card images


From Slack:

"""
Here's  quick update. Still some details to finish up... need to make a pop up window for player options (use default avatars, hide player chat, use green table felt instead of black, etc.), need to add the pot and split pot chip positions, need to get all of the full resolution card images
Feedback welcome!
top left will say the game limit, top right will show a timer on the players turn. On other player's turns, the timer will show in the action bar - where it says "Bet", "Fold", etc.
Chip colors are just done with a div bg color, so chips can be any color, I'll make plenty of preset denominations to keep the stacks from getting to high
Oh, and I have a Dealer Button, I just forgot to put it in this screenshot 

---

noashh 6:49 PM looks good, maybe some buttons with pre set bet amounts? So when I want to bet 50 I can just click on "50" button
hobofife 12:07 AM yea, the slider will automatically snap to preset intervals, depending on the big blind / limit and the player's chip stack
hobofife 12:20 AM Gonna change it to all helvetica/arial/sans serif fonts too 
"""

First the card images, then the dealer button, then the pot chips.

---

Imagemagick and Inkscape commands:

convert -background none 10C.svg 10C.png
convert 10C.png -trim +repage 10C.png
convert 10C.png -resize 100x 10C.png

https://shkspr.mobi/blog/2013/03/inkscape-cropping-svg-files-on-the-command-line/

inkscape --verb=FitCanvasToDrawing --verb=FileSave --verb=FileClose *.svg

Maybe I should resize the svg and then convert to png. It doesn't matter too much since I'm only scaling down, not up, but just for the sake of doing it properly.

^^^ **Nope! Converting SVG files with ImageMagick doesn't really work. I could do it with another inkscape command, but just gonna resize the PNG files, since the original is large enough for what I need.**

I need filenames for the different cards... size1, size2, 4 color...

Ok, maybe make two different directories, one for the normal deck, one for the 4 color deck, and give the larger cards a suffix... 7H-150.png. Okay, doing all cards filenames with the width as a suffix.

1. inkscape fit canvas for all cards
2. convert resize
3. convert to png

All good on the cards. Added color to the card backs to make the player name and chip stack more readable.

# Thu Dec  4 11:14:46 EST 2014

Alright, aside from some modifications requested for the GUI that I'm going to work on at the end, the design of the GUI is all finished. Now to start making things work. I'm going to try to follow the list written up in the spec I provided to 5K and valarmg.

First thing is to get the pot amount to display based on whatever message the server sends. So there are two layers, communicating with the server and updating the GUI.

For the pot amount label:

Update CSS to min-width, not width, so it expands with text. Add left-right padding. Then write JS to recenter label when it is over 120px.

--- 

So I create a WebSocket connection inside of the pangea object. When the WebSocket recieves a message, it parses is as JSON, then iterates through the object's keys, and for each key it matches a key in the handlers object which pairs the key with a function to handle that key. so message = {'potAmount':450.00} will match handlers = {'potAmount':pangea.API.potAmount} and then call pangea.API.potAmount(450.00).	   


# Sun Dec  7 20:45:33 EST 2014

Should rename #bet_slider to #bet-slider

Added an invitation class to each seat... manually, not generated by Python script yet.

# Wed Dec 10 12:29:08 EST 2014

Most of the first milestone is basically complete: the GUI recieves seat info and player info from the server, and each seat has objects for facedown and faceup cards, which all have a a .deal() method, so dealing cards to the players works nice.

Before I move on to dealing the board cards, I just want to tighten things up a bit. Right now I have a test function on the server that fills up the table with players, I'd like to change that to accept a parameter for a max number of players. I also need commands to clear all of the players from the table. Even though this only effects the mock server, not the GUI, I think it will make testing and demonstration easier. Also, I want to start adding HTML buttons to trigger some of the tests and stuff.

The existing JS code is going to need a little reorganization. Just as far as what namespaces different things are in, what different methods are named, how the files are organized, etc.

The main goal before submitting the next milestone is to make sure messages from the server are being processed correctly (any number of API commands in one message, the client will loop through the JSON object, and any number of parameters specified or not for each API entry point ('seat', 'player', etc)). so far this is all good, I just want to make sure nothing breaks as I add more code.

Also, I need code to clear all of the players' cards and the board cards.

# Thu Dec 11 12:08:16 EST 2014

Some problems: the cards won't deal if the player isn't sitting. And I need to clear the cards. And I need to start dealing with the dealer button.

^^ Ok, np, there was an indentation issue in the server side code, the client is fine with dealing even if the player has not joined the table.

Also I need to add player actions.

- Dealer button / Deal in order 
- Fold Cards / Muck cards
- Show cards / Return to deck (should be the same method as fold?)

Done with showing the button, but I need to track the active players and move the button. Well, each seat already has a "playing" attribute. So I need to check the "playing" attr of each seat after the current dealer in order to update the dealer.

Okay, I think I should worry about dealing in order first, then I'll know if I need some kind of seperate array for the active seats.

Ah, I can just make a list of 1-9 starting with the seat after the dealer and then use that as the indexes. like tableOrder = [5,6,7,8,0,1,2,3,4]; for i in tableOrder.length; index = tO[i]; seat = pangea.seats[index]; Then just check if each seat is playing. Then I can update the table order by 1 after the hand, check if each seat is playing in order to place the dealer button, and update the table order again once I have a playing seat with the button, so that seat is in the first position of the tO array.

Yep, added a tableOrder property on the main pangea object and a getTableOrder method to update it.

It all works, but I need the server to specify who the dealer is now. So actually, I don't need to figure out who the dealer is: that is the server's job.

I want a function to return all cards left in player's hands, and I don't want to show the animation for players that aren't holding cards, so I'll add a method on the seat to check for images in their card objects, and check that method inside the returnCards method. That way I can call returnCards on the whole table, but it will only show on the seats holding cards.


# Mon Dec 22 14:27:22 CST 2014

Fuck, trying to sort out what I'm working on... it's been over a week I think since I've worked on this. Pretty sure I'm gonna just work on getting the chips displayed for the player bets. That means getting a player bet amount from the server, updating the label with the numerical display, then calculating what chips to show, and then animating the chips going into the pot. So while I really want to start with displaying chips, maybe I should start with showing the bet label, and then maybe getting the info from the server, or at least writing the api code to handle the message from the server, and then I can worry about the chips.

Yuck, so hard to get started working in a new place, someone else's house, when I haven't donw any real work in over a week. Gotta make this stuff as simple as possible until I get focused and my brain get's all fired up. Maybe gotta turn of the house music for awhile, it's probably done it's job by now and hopefully I can still get an hour or two of silence before anyone comes home and diturbs me. LOL so hard to turn of Kerri Chandler though. 

- make sure bet label HTML elements are there

ok, idk... the bet labels (called 'stack-label' in the HTML because bet-label is the player's bet in the controls) are hidden if they are empty. I need to add that code into the general update and have the 'hide' class removed if the label is not empty.

ok, done.

Alright, adding a 'bet' property to the Seat object. Need to add a selector for the bet and a method to update it.

Yea... just gonna move the hiding of the bet labels into the seat update, not in the general gui update. 

Alright, got the bet's updating through the API, just by adding the 'bet' property to the seat object. Nice when things work out that way. I'm thinking now that I may place the bet label on top of the chip stack, it might look a lot better. We'll see once I display the chips for the bet.

Ok, I have the playerChips code from the mockup. What I need to do now is have it add in a class name for the seat the chips are at, that way I can remove all of the elements with that classname, once they are moved into the pot... but I don't really need to do that, since all of the chips get moved into the pot and removed at the same time... so really, the playerChips code is probably perfectly fine the way it is, and then I can add code to move all of the playerChips into the pot at the same time. I just need to make sure that I can specify a wide range of chipnum classes, to make use of different denominations.

Now I need to add a constant that sets all of the denominations and the class name for each denomination. Or maybe just make the class name whatever the value is? chip10 chip250 chip5000 chip10000. Yea, that will be good. I'll just put default colors in CSS and leave it at that.

# Sun Dec 28 19:17:24 CST 2014

Working on milestone 3:

+ Get opponent bet amounts from server, update GUI
+ Show chips in player stacks based on bet amount
+ Show bet amount in label
+ Animate folded cards
+ Show chips in pot based on pot amount
+ Get opponent action from server
+ Show action in status bar for opponent that just acted
+ Show timer in status bar for opponent in turn 
+ Show pot amount in label

- Show side pot window
- Send player actions to server (fold, check, bet, raise, call, auto options)
- Show countdown timer on player's turn

- Control bet amount by slider control
- Slider control snaps to amounts based on limit/blind, and chip stack
- Auto controls send action to server on player's turn
- Check/Bet update to Call/Raise

