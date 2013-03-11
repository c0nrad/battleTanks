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

class FoodBot(Player):
    def __init__(self):
        super(FoodBot, self).__init__()
        # DON'T PUT STUFF IN HERE
        pass
        
    def init(self):
        self.mVelocityX = 1
        self.mVelocityY = 1
        self.axisSwitch = False
        
    def __str__(self):
        return "FoodBot"

    def getColor(self):
        return (0, 255, 0)
        
    def getMove(self):
        (x, y) = self.getPos()


        if len(self.getFoodPos()) >= 1:
            foodPos = self.getFoodPos()[0]
            (dirX, dirY) = (x - foodPos[0], y - foodPos[1])
            if abs(dirX) > abs(dirY):
                if dirX < 0:
                    return Move.RIGHT
                else:
                    return Move.LEFT
            else:
                if dirY < 0:
                    return Move.DOWN
                else:
                    return Move.UP
        
        # Just do a zig zag if there's no food
        newPos = (x + self.mVelocityX, y + self.mVelocityY) 
        if x == 0:
            self.mVelocityX = 1
        elif (x >= self.BOARD_LENGTH - 1):
            self.mVelocityX = -1

        if y == 0:
            self.mVelocityY = 1
        elif (y >= self.BOARD_HEIGHT - 1):
            self.mVelocityY = -1

        self.axisSwitch = not self.axisSwitch
        if self.axisSwitch:
            if self.mVelocityY == 1:
                return Move.DOWN
            return Move.UP
        else:
            if self.mVelocityX == 1:
                return Move.RIGHT
            return Move.LEFT