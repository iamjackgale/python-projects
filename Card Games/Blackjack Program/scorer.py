#Scoring module that counts the score of a hand, specifically for use in blackjack.

cardScoreDict = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "1":10, "J":10, "Q":10, "K":10}

def countScore(returnHand: list):
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
            score = score + cardScoreDict[suit]
    
    return score

#Add functionality to count dealer's score without giving player option over whether to value ace as 1 or 11

def countDealerScore(returnHand: list):
    dealerScore = 0
    aceCounter = 0

    for card in returnHand:
        suit = str(card[0])
        if suit == "A":
            aceCounter += 1
        else:
            dealerScore = dealerScore + cardScoreDict[suit]
    
    #Can only have 1 x 11, so only first ace matters
    while aceCounter > 0:
        if dealerScore + 11 > 21:
            dealerScore += 1
            aceCounter -= 1
        else:
            dealerScore += 11
            aceCounter -= 1

    return dealerScore