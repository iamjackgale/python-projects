#Card deck module to capture the general functions of a card deck, for use in different types of card games.

from random import seed
from random import shuffle
from random import randint

class Deck():
    cardList = []
    fullDeckList = []
    dict = {}

    #Add function to name the deck for the specific application
    def __init__(self, name):
        self.name = name
    
    #Add function to reset to a new clean deck in perfect order
    def newDeck(self):
        Deck.cardList = []

        #Prepare list card values
        cardValueList = []
        for n in range(2,11):
            cardValueList.append(str(n))
        cardValueList += ['J','Q','K','A']
        ###print(cardValueList)

        #Next list of 4 suits
        cardSuitList = ['H','D','S','C']

        #Next combine suits and unique values for 52 cards
        for b in cardSuitList:
            for a in cardValueList:
                Deck.cardList.append(str(a)+str(b))
                Deck.fullDeckList.append(str(a)+str(b))
        return "New deck generated."

    #Add function to show the current arrangement of the deck
    def showDeck(self):
        if type(Deck.cardList) != None:
            return Deck.cardList
        else:
            return "A new deck has not yet been generated. Please use deck.newDeck() to generate a new deck first."

    #Add function to randomise arrangement of the deck
    def shuffleDeck(self):
        if type(Deck.cardList) != None:
            seed(seed(1))
            shuffle(Deck.cardList)
            return "Deck shuffled."
        else:
            return "A new deck has not yet been generated. Please use deck.newDeck() to generate a new deck first."

    #Add function to withdraw the first card from the deck (returning the name of the card)
    def drawCard(self):
        if len(Deck.cardList) > 0:
            _return = Deck.cardList[0]
            Deck.cardList.remove(Deck.cardList[0])
            return _return
        else:
            return "There are no more cards to draw. Please return cards to the deck or generate a new deck."

    #Add function to return a designated card to the top of the deck
    def returnCardTop(self, card):
        if (card in Deck.fullDeckList) == True:
            _cardList = Deck.cardList
            _card = [card]
            Deck.cardList = _card + _cardList
            return "Card returned to the top of the deck."
        else:
            return "The inputted value is not a recognised card. Please consult the cardList to see the list of recognised cards"
    
    #Add function to return a designated card to the bottom of the deck
    def returnCardBottom(self, card):
        if (card in Deck.fullDeckList) == True:
            _cardList = Deck.cardList
            _card = [card]
            Deck.cardList = _cardList + _card
            return "Card returned to the bottom of the deck."
        else:
            return "The inputted value is not a recognised card. Please consult the cardList to see the list of recognised cards"

    #Add function to place the card at a specified location in the deck
    def returnCardSpecific(self, card, location):
        _length = len(Deck.cardList)
        if (card in Deck.fullDeckList) == True and 0 <= location <= _length:
            split1 = []
            split2 = []
            for a in Deck.cardList:
                if Deck.cardList.index(a) <= location:
                    split1.append(a)
                else:
                    split2.append(a)
            split1.append(card)
            Deck.cardList = split1 + split2
            return "Card returned to the specified location in the deck."
        elif (card in Deck.cardList) == False:
            return "The inputted value is not a recognised card. Please consult the cardList to see the list of recognised cards"
            if location > len(Deck.cardList) or location <= 0:
                return "The inputted location is not available. Check the total number of cards in the deck and use an integer value between 1 and the total."
        elif location > len(Deck.cardList) or location <= 0:
            return "The inputted location is not available. Check the total number of cards in the deck and use an integer value between 1 and the total."
        
    #Add function to place the card at a random location in the deck
    def returnCardRandom(self, card):
        if (card in Deck.fullDeckList) == True:
            seed(1)
            _randomLocation = randint(0,52)
            split1 = []
            split2 = []
            for a in Deck.cardList:
                if Deck.cardList.index(a) <= _randomLocation:
                    split1.append(a)
                else:
                    split2.append(a)
            split1.append(card)
            Deck.cardList = split1 + split2
            return "Card returned to a random location in the deck."
        else:
            return "The inputted value is not a recognised card. Please consult the cardList to see the list of recognised cards"

    #Add function to generate or otherwise return a dictionary of unique card numbers
    def deckDict(self):
        #Generate unique card numbers for use with dictionary
        cardNumberList = list(range(1,53))

        #Generate dictionary reconciling unique card numbers to cardList
        for numb in cardNumberList:
            _value = Deck.fullDeckList[numb-1]
            Deck.dict[numb] = _value

        return "Deck dictionary generated/reset."