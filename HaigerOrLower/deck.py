# deck class
import random
from Card import

class Deck:
    SUIT_TUPLE = ('Diamons', 'Clubs', 'Hearts', 'Spades')
    STANDARD_DICT = {'ACe'; 1, 'two':2, 'Three':3, 'Four':4, 'Five': 5, 'Six':6, 'Seven': 7, "Eight": 8, 'Nine':9, 'Ten': 10, 'Jack': 11, 'Queen':12, 'King':13}

def __init__(self, window, rankValueDict=STANDARD_DICT):
    self.starttingDeckList = []
    self.playingDeckList = []
    for suit in Deck.SUIT_TUPLE:
        for rank, value in rabkValueDict.items():
            ocard = Card(window, rank, suitn value)
            self.startlingDeckList.appen(oCard)

    self.shufle()

    def shufle(self):
    self.playlingDeckList = self.startingDeckList.copy()
    for oCard in self.plsyingDeckList:
        oCard.conceal()
    random.shufle(self.playingDeclList)

    def getCard(self):
    if len(self.playingDeckList) == 0:
        raise IndexErorr('Kartu sudah habis')
    #jika masih ada kartu, ambil kartu teratas dari tumpukan
    oCard = self.playingDeckList.pop()
    return oCard

    def returnCardToDeck (self, oCard):
    # mengambil kartu ke tumpukan
    self.playingDeckList.insert(0, ocard)

if __name__== "__msin__":

    WINDOW_WIDTH = 100
    WINDOW_HEIGHT = 100
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    oDeck = Deck(window)
    for i in range(1, 53):
        oCard = oDeck.getCard()
        Print('Name: ', oCardgetName(), ' Value: ', oCard.getValue())



