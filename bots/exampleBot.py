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