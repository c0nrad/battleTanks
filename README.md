Battle Tanks
=========

![battleTanks Gameplay](https://raw.github.com/c0nrad/battleTanks/master/gamePlay.png)

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

```python
from player import Player
from debug import *

# This enumeration is how you specify what direction you want the tank to move.
# For example Move.UP means up, Move.RIGHT means right.
class Move:
    UP, DOWN, LEFT, RIGHT = range(4)

# Here is a bare bones example bot. It needs to extend class Player
class ExampleBot(Player):

    def __init__(self):
        # Make sure that the name of your Bot is in this function
        # But do not put anything else in here
        super(Example, self).__init__()
        pass

    # In this function you can put whatever you need before the game starts.
    # This function will only be called once
    def init(self):
        print "hello world, once!"

    # This function is how you get to name your Bot
    def __str__(self):
        return "BareBonez"

    # The color of your tank, specified in (R G B)
    def getColor(self):
        return (0, 255, 0)

    # This is the meat of your bot. This function must return either Move.UP, Move.DOWN, Move.LEFT, Move.RIGHT
    def getMove(self):
        return Move.DOWN
```
3. You must add your bot to the game via file battleTanks.py.
    1. Add the import statement at the top of the file
    2. Create a new instance of it next to the other bots
    3. Make sure a instance of your bot is passed to the board

4. Then run the game by the command _make run_ from terminal.

Useful Functions
-

