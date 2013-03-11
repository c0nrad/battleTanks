# Include your bot here
from bots.player import Player
from bots.bounceBot import BounceBot
from bots.wallBot import WallBot
from bots.foodBot import FoodBot

from PyQt4 import Qt
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import *

from board import Board
import sys

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    app.connect(app, SIGNAL("lastWindowClosed()"), app, SLOT("quit()"))

    # Create an instance of your bot here
    bounceBot = BounceBot()
    wallBot = WallBot()
    foodBot = FoodBot()

    # In this list are the bots that will be battling. Up to 4
    bots = [ wallBot, foodBot]

    # Play game!
    board = Board(bots)
    
    sys.exit(app.exec_())
