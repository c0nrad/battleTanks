from debug import *

class Move:
    UP, DOWN, LEFT, RIGHT = range(4)
        
class Player(object):
    def __init__(self):
        
        self.LENGTH = 5
        self.BOARD_HEIGHT = 24
        self.BOARD_LENGTH = 32
        
        self.mNodes = []
        
        for x in range(self.LENGTH):
            self.mNodes.append((0, 0,))

        self.switch = False
            
    def setStartPos(self, pos):
        self.mNodes = []
        for x in range(self.LENGTH):
            self.mNodes.append(pos)
        
    def __str__(self):
        return "Default Bot"
        
    def getMove(self):
        if self.switch:
            self.switch = not self.switch
            return Move.RIGHT
        else:
             self.switch = not self.switch
             return Move.DOWN

    def getColor(self):
        return (255, 0, 0)

    def setGame(self, game):
        self.mGame = game

    def getPos(self):
        return self.mNodes[0]
        
if __name__ == "__main__":
    p = Player()
    print p.getMove()
    