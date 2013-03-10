import sys
import time
from debug import *
from random import randrange

from PyQt4 import Qt
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import *

# BOTS
from player import Player
from bounceBot import BounceBot
from wallBot import WallBot

class Move:
    UP, DOWN, LEFT, RIGHT = range(4)

class Board(QtGui.QWidget):
    
    def __init__(self, players):
        super(Board, self).__init__()
        self.mPlayers = players

        self.SQUARE_SIZE = 25
        self.GAME_WIDTH_SQUARES = 32
        self.GAME_HEIGHT_SQUARES = 24
        self.SCENE_HEIGHT = 2 + self.SQUARE_SIZE * self.GAME_HEIGHT_SQUARES
        self.SCENE_WIDTH = 2 + self.SQUARE_SIZE * self.GAME_WIDTH_SQUARES
    
        self.mScene =  QGraphicsScene(0, 0, self.SCENE_WIDTH, self.SCENE_HEIGHT)
        self.mView = QGraphicsView(self.mScene)
        self.initUI()

        self.mPlayerRectsMap = dict()

        # Little cheat so that startGame is called once the event engine is processing events (return app.exec())
        QTimer.singleShot(0, self.startGame)

    def getPlayerPosistions(self):
        return [p.mNodes[0] for p in self.mPlayers]

    def getGameBoardSize(self):
        return (self.GAME_WIDTH_SQUARES, self.GAME_HEIGHT_SQUARES)
        
    def initUI(self):      
        self.setWindowTitle('Tanks')
        layout = QVBoxLayout()
        layout.addWidget(self.mView)
        self.setLayout(layout)
        self.show()

    def startGame(self):
        goodMessage("board::startGame: initalizing players!") 
        for player in self.mPlayers:
            infoMessage(player, " has joined the game!")
            self.drawPlayer(player)
            player.setStartPos( ((randrange(0, self.GAME_WIDTH_SQUARES)), randrange(0, self.GAME_HEIGHT_SQUARES)))
            player.init()
            
        qApp.processEvents()
        players = self.mPlayers
                    
        while True:
            alivePlayers = [p for p in self.mPlayers if p.isAlive]

            if len(alivePlayers) == 1:
                goodMessage(alivePlayers[0], " has won the game!")
                break
            elif len(alivePlayers) == 0:
                warningMessage("board::startGame: everyone died.. you guys suck")
                break

            for player in alivePlayers:
                move = player.getMove()

                self.movePlayer(player, move)
                qApp.processEvents()
                time.sleep(.01)
                qApp.processEvents()

                if not self.isValidMove(player, player.mNodes[0]):
                    warningMessage("board::startGame: ", player, " has commited an illegal move")
                    player.isAlive = False

                deadPlayer = self.isHitPlayer(player, player.mNodes[0])
                if deadPlayer in alivePlayers:
                    warningMessage("board::startGame: ", player, "has hit ", deadPlayer)
                    deadPlayer.isAlive = False

            self.updateBoard()

    def isHitPlayer(self, player, move):
        for p in [p for p in self.mPlayers if not p == player]:
            for n in p.mNodes[1:]:
                if n == move:
                    return p
            
    def updateBoard(self):
        self.mScene.clear()
        alivePlayers = [p for p in self.mPlayers if p.isAlive]
        
        for p in alivePlayers:
            self.drawPlayer(p)

    def movePlayer(self, player, move):
        curPos = player.mNodes[0]

        if move == Move.UP:
            newPos = (curPos[0], curPos[1] - 1)
        elif move == Move.RIGHT:
            newPos = (curPos[0] + 1, curPos[1])
        elif move == Move.LEFT:
            newPos = (curPos[0] - 1, curPos[1])
        elif move == Move.DOWN:
            newPos = (curPos[0], curPos[1] + 1)
        else:
            errorMessage(move, " is not a valid move dumbass")

        player.mNodes = [newPos] + player.mNodes[:-1]
        
    def isValidMove(self, player, pos):
        if pos[0] < 0 or pos[0] >= 32:
            return False
        if pos[1] < 0 or pos[1] >= 24:
            return False
        return True
                
    def drawPlayer(self, player):
        playerTup = player.getColor()
        rectColor = QColor(playerTup[0], playerTup[1], playerTup[2])
        brush = QBrush(rectColor)
        for n in player.mNodes:
            (x, y) = self.convertCoords(n)
            self.mScene.addRect(x, y, 23, 23, QPen(), brush)

    def convertCoords(self, coords):
        return ( coords[0] * 25 + 1, coords[1] * 25 + 1)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    app.connect(app, SIGNAL("lastWindowClosed()"), app, SLOT("quit()"))
    p = BounceBot()
    p3 = WallBot()
    g = Board([p, p3])
    
    sys.exit(app.exec_())

