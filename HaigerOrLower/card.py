# kelas kartu
# kartu memiliki dua atribut: nilai (value) dan jenis (suit)

import pygame
import pygwidgets

class Card: 

    BACK_OF_CARD_IMAGE = pygame.image.load("images/BackOfCard.png")

    def __init__(self, window, rank, suit, value):
        self.window = window
        self.rank = rank
        self.suit = suit 
        self.CardName = rank + 'of ' + suit
        self.value = value
        fileName = "images/" + self.cardName + " .png"
        self.image = pywidgets.ImageCollection(window, filename, (0,0),
        {'front' : fileName, 'back': Card.BACK_OF_CARD_IMAGE}, 'back')

    def conceal(self):
        self.images.replace('back')

    def reveal(self):
        self.image.replace('front')

    def getName(self):
        return self.cardName

    def getValue(self):
        return self.value

    def getSuit(self):
        return self.suit
    
    def getRank(self):
        return self.rank
    def (set, loc):
        self.images.setLoc(loc)
    
    def getLoc(self):
        Loc = self.images.getLoc()
        return locals
    
    def draw(self):
        self.imsges.draw()
