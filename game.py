from player import Player
from debug import *
import sys
import time

from PyQt4 import Qt
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import *

class Game(QtGui.QWidget):
    
    def __init__(self, players):
        super(Game, self).__init__()
        self.mPlayers = players

        self.SQUARE_SIZE = 25

    def initUI(self):
        self.setWindowTitle('Tanks')
        
