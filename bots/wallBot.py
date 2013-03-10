from player import Player
from debug import *

# Helpful functions:
#
# self.LENGTH
#    The length of your snake
#
# self.BOARD_HEIGHT
#    The height of the board
#
# self.BOARD_LENGTH
#    The length of the board
#
# self.getPos():
#    Returns the posision of your head node. (x, y) 

class Move:
    UP, DOWN, LEFT, RIGHT = range(4)

class WallBot(Player):
    def __init__(self):
        super(WallBot, self).__init__()
        # DON'T PUT STUFF IN HERE
        pass
        
    def init(self):
        self.mDirection = Move.DOWN
        
    def __str__(self):
        return "IMAWALLBOT"

    def getColor(self):
        return (0, 0, 255)
        
    def getMove(self):
        (x, y) = self.getPos()

        if self.mDirection == Move.DOWN:
            if y == self.BOARD_HEIGHT - 1:
                self.mDirection = Move.RIGHT
        elif self.mDirection == Move.RIGHT:
            if x == self.BOARD_LENGTH - 1:
                self.mDirection = Move.UP
        elif self.mDirection == Move.UP:
            if y == 0:
                self.mDirection = Move.LEFT
        elif self.mDirection == Move.LEFT:
            if x == 0:
                self.mDirection = Move.DOWN

        return self.mDirection