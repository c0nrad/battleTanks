from bots.player import Player
from bots.bounceBot import BounceBot
from bots.wallBot import WallBot

from PyQt4 import Qt
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import *

from board import Board
import sys

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    app.connect(app, SIGNAL("lastWindowClosed()"), app, SLOT("quit()"))

    bounceBot = BounceBot()
    wallBot = WallBot()
    bots = [bounceBot, wallBot]
    board = Board(bots)
    
    sys.exit(app.exec_())
