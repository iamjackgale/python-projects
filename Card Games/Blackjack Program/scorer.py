#Scoring module that counts the score of a hand, specifically for use in blackjack.

def countScore(returnHand: list):
  
    cardScoreDict = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
    
    score = 0

    for card in returnHand:
        suit = str(card[0])
        if suit == "A":
            breaker = 0
            while breaker == False:
                value = int(input("Select the value of an Ace (either 1 or 11): "))
                if value == 1:
                    score += value
                    breaker = True
                elif value == 11:
                    score += value
                    breaker = True
        else:
            score += cardScoreDict[suit]
    
    return score