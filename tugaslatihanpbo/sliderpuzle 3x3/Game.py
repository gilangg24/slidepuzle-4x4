STARTING_OPEN_SQUARE_NUMBER = 8
from Square import *
import random
import os
import pygame

class Game():
    START_LEFT = 35
    START_TOP = 35

    def __init__(self, window):
        self.window = window

        LEGAL_MOVES_DICT = {
            0: (1, 3),
            1: (0, 2, 4),
            2: (1, 5),
            3: (0, 4, 6),
            4: (1, 3, 5, 7),
            5: (2, 4, 8),
            6: (3, 7),
            7: (4, 6, 8),
            8: (5, 7)
        }

        yPos = Game.START_TOP
        self.squareList = []

        for row in range(0, 3):
            xPos = Game.START_LEFT
            for col in range(0, 3):
                squareNumber = (row * 3) + col
                legalMovesTuple = LEGAL_MOVES_DICT[squareNumber]
                oSquare = Square(self.window, xPos, yPos, squareNumber, legalMovesTuple)
                self.squareList.append(oSquare)
                xPos = xPos + SQUARE_WIDTH
            yPos = yPos + SQUARE_HEIGHT

        base_path = os.path.abspath(os.path.dirname(__file__))
        sounds_path = os.path.join(base_path, 'sounds')

        self.soundTick = pygame.mixer.Sound(os.path.join(sounds_path, 'tick.wav'))
        self.soundApplause = pygame.mixer.Sound(os.path.join(sounds_path, 'applause.wav'))
        self.soundNope = pygame.mixer.Sound(os.path.join(sounds_path, 'nope.wav'))

        self.playing = False
        self.startNewGame()

    def startNewGame(self):
        for oSquare in self.squareList:
            oSquare.reset()

        self.oOpenSquare = self.squareList[STARTING_OPEN_SQUARE_NUMBER]

        for i in range(0, 200):
            legalMovesForThisTile = self.oOpenSquare.getLegalMoves()
            nextMoveNumber = random.choice(legalMovesForThisTile)
            print("OpenSquare:", self.oOpenSquare.getSquareNumber())
            print("LegalMoves:", legalMovesForThisTile)
            print("Next move:", nextMoveNumber)
            print("Jumlah squareList:", len(self.squareList))
            oSquare = self.squareList[nextMoveNumber]

            self.switch(oSquare, playMoveSound=False)

        self.playing = True

    def gotClick(self, clickLoc):
        if not self.playing:
            return

        for oSquare in self.squareList:
            if oSquare.clickedInside(clickLoc):
                squareNumber = oSquare.getSquareNumber()
                legalMovesForOpenSquareTuple = self.oOpenSquare.getLegalMoves()
                legalMove = squareNumber in legalMovesForOpenSquareTuple
                if legalMove:
                    self.switch(oSquare, playMoveSound=True)
                else:
                    self.soundNope.play()
                return

    def switch(self, oSquareToSwitch, playMoveSound=False):
        oSquareToSwitch.switch(self.oOpenSquare)
        self.oOpenSquare = oSquareToSwitch

        if playMoveSound:
            self.soundTick.play()

    def checkForWin(self):
        if not self.playing:
            return False

        for oSquare in self.squareList:
            if not oSquare.isTileProperPlace():
                return False

        self.playing = False
        self.soundApplause.play()
        return True

    def getGamePlaying(self):
        return self.playing

    def draw(self):
        print("Game.draw called")
        for oSquare in self.squareList:
            oSquare.draw()
