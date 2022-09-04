#Card hand module to capture the functionality of a player's hand of cards, for use in different types of card games.

class Hand():

    #Add function to name the hand for the specific application
    def __init__(self, name: str):
        self.name = name
        self.handCardList = []
        print("Hand added.")
    
    def drawCard(self, card):
        self.handCardList.append(card)
        print("Card added to " + str(self.name) +"'s hand.")

    def showHand(self):
        print(self.handCardList)

    def returnHand(self):
        return self.handCardList
    
    def discardCard(self, card):
        self.handCardList.pop(card)
        print("Card discarded from hand.")

    def discardAll(self):
        discardedCards = self.handCardList
        self.handCardList = []
        print("Hand discarded")
        return discardedCards