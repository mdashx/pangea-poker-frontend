Okay, I'm trying to place the seats at the poker table, and I'm writing a script to calculate points and write out CSS, so I can easily change things, if for instance the center point of the table or size of the table image changes, or if we need more or less seats, etc.

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


