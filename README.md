Battle Tanks
=========

Battle Tanks is a AI framework for creating simple Bots and Learning Python.

The Game
-

The object of the game is to collect points. Points can be collected in two different ways:
 * 1 Point: Collecting Food
 * 3 Points: Killing an opponent

The game ends when there is only one tank alive. To kill an enemy tank, your tanks head must hit the other tanks body. Hitting head on head will kill both of the tanks.

Constants
-

Length of Tanks: 7
Board Size: 20 - 32
Points Per Kill: 3
Points Per Food: 1

How To Play
-

To play you must constuct a bot. There are three example bots in the bots/ folder. But to create a bot you must do the following:

1. Create a new python file, example _sclarsenBot.py_ within the bots folder.
2. Your bot implement a few functions and extend the Player class. A bare bones bot is show below

3. BARE BONES

3. You must add your bot to the game via file battleTanks.py.
    1. Add the import statement at the top of the file
    2. Create a new instance of it next to the other bots
    3. Make sure a instance of your bot is passed to the board

4. Then run the game by the command _make run_ from terminal.

Useful Functions
-

