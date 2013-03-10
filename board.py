import sys
import time
from debug import *
from random import randrange

from PyQt4 import Qt
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import *

# BOTS
from bots.player import Player
from bots.bounceBot import BounceBot
from bots.wallBot import WallBot

class Move:
    UP, DOWN, LEFT, RIGHT = range(4)

class Board(QtGui.QWidget):
    
    def __init__(self, players):
        super(Board, self).__init__()
        self.mPlayers = players

        self.SQUARE_SIZE = 25
        self.GAME_WIDTH_SQUARES = 32
        self.GAME_HEIGHT_SQUARES = 20
        self.STATS_HEIGHT = 100
        self.SCENE_HEIGHT = 2 + self.SQUARE_SIZE * self.GAME_HEIGHT_SQUARES + self.STATS_HEIGHT
        self.SCENE_WIDTH = 2 + self.SQUARE_SIZE * self.GAME_WIDTH_SQUARES
        self.COUNT_PER_NEW_FOOD = 100
        self.POINTS_PER_KILL = 3
    
        self.mScene =  QGraphicsScene(0, 0, self.SCENE_WIDTH, self.SCENE_HEIGHT)
        self.mView = QGraphicsView(self.mScene)
        self.initUI()

        self.mFoodPos = []

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

        gameCounter = 0
        while True:
            gameCounter += 1
            alivePlayers = [p for p in self.mPlayers if p.isAlive]
            
            # See if the Game is over
            if len(alivePlayers) <= 1:
                goodMessage("GAME OVER")
                for p in self.mPlayers:
                    goodMessage(p,": ", p.mPoints)
                break
           
            # Handle Food
            if gameCounter % self.COUNT_PER_NEW_FOOD == 1:
                foodPos = ((randrange(0, self.GAME_WIDTH_SQUARES)), randrange(0, self.GAME_HEIGHT_SQUARES))
                self.mFoodPos.append(foodPos)
                for p in self.mPlayers:
                    p.mFoodPos = self.mFoodPos

            for food in self.mFoodPos:
                self.drawFood(food)

            # Handle Players
            for player in alivePlayers:
                # Get the New Move
                move = player.getMove()
                self.movePlayer(player, move)
                qApp.processEvents()
                time.sleep(.01)
                qApp.processEvents()

                # Hit Wall
                if not self.isValidMove(player, player.mNodes[0]):
                    warningMessage("board::startGame: ", player, " has commited an illegal move")
                    player.isAlive = False

                # Hit Self
                if len(set(player.mNodes)) != player.LENGTH and gameCounter > player.LENGTH:
                    warningMessage("board::startGame: ", player, " hit himself...")
                    
                # Hit Player
                deadPlayer = self.isHitPlayer(player, player.mNodes[0])
                if deadPlayer in alivePlayers:
                    warningMessage("board::startGame: ", player, " has hit ", deadPlayer)
                    deadPlayer.isAlive = False
                    player.mPoints += self.POINTS_PER_KILL

                # Hit Food
                for food in self.mFoodPos:
                    if food == player.mNodes[0]:
                        player.mPoints += 1
                        self.mFoodPos.remove(food)
                        for player in self.mPlayers:
                            player.mFoodPos = self.mFoodPos
                    
            self.updateBoard()
            self.drawGameCount(gameCounter)

    def isHitPlayer(self, player, move):
        for p in [p for p in self.mPlayers if not p == player]:
            for n in p.mNodes:
                if n == move:
                    return p

    def drawFood(self, pos):
        color = QColor(255, 255, 0)
        size = 23
        pos = self.convertCoords(pos)
        self.mScene.addEllipse(pos[0], pos[1], size, size, QPen(), QBrush(color))
        
    def drawStats(self):
        self.mScene.addLine(0, self.SCENE_HEIGHT - self.STATS_HEIGHT, self.SCENE_WIDTH, self.SCENE_HEIGHT - self.STATS_HEIGHT)

        for pIndex in range(len(self.mPlayers)):
            p = self.mPlayers[pIndex]
            font = QFont()
            playerTup = p.getColor()
            textColor = QColor(playerTup[0], playerTup[1], playerTup[2])

            # Draw The Name
            font.setPointSize(14)
            textItem = self.mScene.addText(str(p), font)
            textItem.setDefaultTextColor(textColor)
            textItem.setPos(pIndex * self.SCENE_WIDTH/4, self.SCENE_HEIGHT - self.STATS_HEIGHT + 5)
            self.mScene.addLine((pIndex + 1) * self.SCENE_WIDTH/4, self.SCENE_HEIGHT - self.STATS_HEIGHT,
                                (pIndex + 1) * self.SCENE_WIDTH/4, self.SCENE_HEIGHT)

            # Draw the points
            points = p.mPoints
            font.setPointSize(10)
            textItem = self.mScene.addText("Points: " + str(points), font)
            textItem.setDefaultTextColor(textColor)
            textItem.setPos(pIndex * self.SCENE_WIDTH/4, self.SCENE_HEIGHT - self.STATS_HEIGHT + 5 + 25)

            # Draw the posistion
            pos = p.getPos()
            font.setPointSize(10)
            textItem = self.mScene.addText("Pos: " + str(pos), font)
            textItem.setDefaultTextColor(textColor)
            textItem.setPos(pIndex * self.SCENE_WIDTH/4, self.SCENE_HEIGHT - self.STATS_HEIGHT + 5 + 45)

    def drawGameCount(self, count):
        font = QFont()
        textColor = QColor(255, 0, 0)
        font.setPointSize(14)
        textItem=self.mScene.addText(str(count), font)
        textItem.setDefaultTextColor(textColor)
        textItem.setPos(self.SCENE_WIDTH - 45, self.SCENE_HEIGHT - self.STATS_HEIGHT - 30)
        
    def updateBoard(self):
        self.mScene.clear()
        self.drawStats()

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
        if pos[0] < 0 or pos[0] >= self.GAME_WIDTH_SQUARES:
            return False
        if pos[1] < 0 or pos[1] >= self.GAME_HEIGHT_SQUARES:
            return False
        return True
                
    def drawPlayer(self, player):
        playerTup = player.getColor()
        rectColor = QColor(playerTup[0], playerTup[1], playerTup[2])
        brush = QBrush(rectColor)
        for n in player.mNodes:
            (x, y) = self.convertCoords(n)
            self.mScene.addRect(x, y, self.SQUARE_SIZE , self.SQUARE_SIZE , QPen(), brush)

    def convertCoords(self, coords):
        return ( coords[0] * 25 + 1, coords[1] * 25 + 1)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    app.connect(app, SIGNAL("lastWindowClosed()"), app, SLOT("quit()"))
    p = BounceBot()
    p3 = WallBot()
    g = Board([p, p3])
    
    sys.exit(app.exec_())

