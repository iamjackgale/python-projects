from time import sleep
import deck
import hand
import scorer #Can move this inside a general BlackJack functions file?

def blackjack():
    GameDeck = deck.Deck("GameDeck")
    GameDeck.newDeck()
    sleep(0.5)
    GameDeck.shuffleDeck()

    #Configure hands
    sleep(0.5)
    player = hand.Hand('Player')
    sleep(0.5)
    dealer = hand.Hand('Dealer')

    #Deal hands
    sleep(0.5)
    card = GameDeck.drawCard()
    player.drawCard(card)
    sleep(0.5)
    card = GameDeck.drawCard()
    dealer.drawCard(card)
    sleep(0.5)
    card = GameDeck.drawCard()
    player.drawCard(card)
    sleep(0.5)
    card = GameDeck.drawCard()
    dealer.drawCard(card)

    #Player's Go
    sleep(0.5)
    print("Player, it's your go.")
    sleep(0.5)
    player.showHand()
    sleep(0.5)
    cardsInHand = player.returnHand()
    handScore = scorer.countScore(cardsInHand)
    if handScore == 21:
        pass
    else:
        while handScore < 22:
            print(f"Player, the value of your hand is { handScore }.")
            sleep(0.5)
            print("Would you like to hit?")
            decision = input("Insert Y for Hit, or N for Stick: ")
            if decision == "Y":
                    sleep(0.5)
                    card = GameDeck.drawCard()
                    player.drawCard(card)
                    cardsInHand = player.returnHand()
                    sleep(0.5)
                    player.showHand()
                    sleep(0.5)
                    handScore = scorer.countScore(cardsInHand)
            elif decision == "N":
                break
            else:
                print("Invalid Input.")
    sleep(0.5)
    if handScore > 21:
        print(f"Hand is worth { handScore }. You are bust!")
        playerScore = handScore
    elif handScore == 21:
        print("Blackjack! You win!")
        playerScore = handScore
    else:
        print(f"End of player's go. Hand is worth { handScore }.")
        playerScore = handScore

    #Dealer's Go
    sleep(0.5)
    print("Dealer, it's your go.")
    sleep(0.5)
    dealer.showHand()
    sleep(0.5)
    cardsInHand = dealer.returnHand()
    handScore = scorer.countDealerScore(cardsInHand)
    if playerScore > 21:
        print("Dealer sticks.")
    elif handScore == 21:
        pass
    else:
        while handScore < 22:
            if handScore < 16:
                print("Dealer hits.")
                sleep(0.5)
                card = GameDeck.drawCard()
                dealer.drawCard(card)
                cardsInHand = dealer.returnHand()
                sleep(0.5)
                dealer.showHand()
                sleep(0.5)
                handScore = scorer.countDealerScore(cardsInHand)
            else:
                print("Dealer sticks.")
                break
    if handScore > 21:
        print(f"Hand is worth { handScore }. Dealer is bust!")
        dealerScore = handScore
    elif handScore == 21:
        print("Blackjack!")
        dealerScore = handScore
    else:
        print(f"End of player's go. Hand is worth { handScore }.")
        dealerScore = handScore
    
    #Evaluation
    print(f"Player's score is { playerScore}.")
    print(f"Dealer's score is { dealerScore}.")
    if dealerScore > playerScore:
        print("Dealer wins!")
    elif dealerScore == playerScore:
        if playerScore == 21:
            print("Player wins!")
        else:
            print("It's a draw!")
    else:
        print("Player wins!")

# Improvements
# - When dealer receives Ace, player is allowed to pick score of 1 or 11. Should automatically choose the best option for the dealer.
# - 
