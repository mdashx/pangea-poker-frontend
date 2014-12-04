The milestones are broken down into:

- Setting up a table and dealing cards
- Getting player actions, betting, updating chips
- Chat, GUI modifications, any details missed in previous milestones

For each milestone, I will make the listed features as fully functional as possible. There could be minor things that I miss, or certain things I can't do until later features are added. In these cases, I will cross all of the t's and dot all of the i's before the final milestone.

I've tried to make the description of the work for each milestone pretty detailed. The basic idea is that all game actions need to be recieved from the server or sent to the server, and the GUI updated. In addition, there are some things that only concern the GUI, for instance, auto-play options will not be sent to the server, they will be used to send the player action to the server when it is the player's turn. Also, all game elements need to be cleared, in some cases from the server, and in some cases by the frontend.

The goal is for the server to completely control game play details and the frontend to control GUI details. So the frontend will not update bet amounts unless the command comes from the server, and the server does not need to worry about updating various GUI elements, just sending the right data. For example, if a player chooses to hide chips and just use large labels in their place, the server doesn't need to know, it just needs to send the correct amount for each player's bet and for the pot.

I will make sure everything works before determining the final milestone complete, and after recieving payment for the final milestone, I will be available to provide any additional support and to make minor changes. I expect to stay involved in the project for the long-term, but at the very least I'll guarantee 60 days of support. However, I will not include additional requirements in the final milestone. For example, adding support for other types of poker games would fall out of the agreed on project scope and would have to wait until the current milestones are complete.

# Milestone 2

Set new hand:

- Set pot to 0
- Set side pots to 0
- Get player info for all seats, update GUI
- Remove all chips from table
- Remove all cards from table
- Remove all player/opponent cards
- Set 'To Call' to 0
- Remove dealer button from table
- Remove bet labels

Set empty table:

- Set new hand
- Get game type / limit / blinds from server, update GUI
- Set all seats to empty
- Remove dealer button from GUI
- Clear all chat *(milestone 4)*
- Hide player controls

Join table:

- Add 'Join' button to GUI
- Send 'Join' to server
- Get 'Join' confirmation from server
- Add player controls to GUI

Player info (based on seat number):

- Get opponent status (active/folded/sitting out/seat empty)
- Get opponent avatar from server and update GUI
- Get opponent name from server and update GUI
- Get opponent chip stack and update GUI

Dealing:

- Get dealer button position from server, update GUI
- Get active opponents from server, update GUI (deal facedown cards)
- Get player hole cards from server, update GUI (show faceup cards)
- Get flop from server, update GUI
- Get turn from server, update GUI
- Get river from server, update GUI
- Get opponent show / muck from server, update GUI
- Animate folded cards
- Get opponents' revealed cards from server, update GUI

# Milestone 3

Player Actions / Betting:

- Get opponent action from server
- Show action in status bar for opponent that just acted
- Show timer in status bar for opponent in turn 
- Get opponent bet amounts from server, update GUI
- Show chips in player stacks based on bet amount
- Show bet amount in label
- Animate folded cards
- Show chips in pot based on pot amount
- Show pot amount in label
- Show side pot window
- Send player actions to server (fold, check, bet, raise, call, auto options)
- Show countdown timer on player's turn
- Control bet amount by slider control
- Slider control snaps to amounts based on limit/blind, and chip stack
- Auto controls send action to server on player's turn
- Check/Bet update to Call/Raise

# Milestone 4

Chat:

- Send chat to server
- Show chat from server
- Disable chat (player, dealer, player and dealer)

GUI Modifications:

- 4 color deck with simplified cards
- Additional background images (table felt and carpet)
- Disable chip images, just show bet amount
- Custom bet amount buttons (30%, etc)
- Preset table positions for 2 and 6 player games
- Option to hide empty seats in 2 and 6 player games