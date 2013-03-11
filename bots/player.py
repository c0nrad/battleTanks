from debug import *

class Move:
    UP, DOWN, LEFT, RIGHT = range(4)
        
class Player(object):
    def __init__(self):
        
        self.LENGTH = 8
        self.BOARD_HEIGHT = 20
        self.BOARD_LENGTH = 32
        
        self.mNodes = [(0, 0)] * self.LENGTH

        self.isAlive = True
        self.mPoints = 0

        self.mFoodPos = []
        
    def setStartPos(self, pos):
        self.mNodes = [pos] * self.LENGTH
        
    def __str__(self):
        return "Default Bot"
        
    def getMove(self):
        return Move.DOWN

    def getColor(self):
        return (255, 0, 0)

    def setGame(self, game):
        self.mGame = game

    def getPos(self):
        return self.mNodes[0]

    def getFoodPos(self):
        return self.mFoodPos

    def getAllPlayerPos(self):
        return self.mAllPlayerPos
        
if __name__ == "__main__":
    p = Player()
    print p.getMove()
    