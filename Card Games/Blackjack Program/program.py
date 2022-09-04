import asyncio
import intro
import deck
import hand
import scorer #Can move this inside a general BlackJack functions file?

if __name__ == "__main__":
    asyncio.run(intro.intro())
    GameDeck = deck.Deck("GameDeck")
    GameDeck.newDeck()
    GameDeck.shuffleDeck()

    #Configure hands
    player = hand.Hand('Player')
    dealer = hand.Hand('Dealer')

    #Deal hands
    card = GameDeck.drawCard()
    player.drawCard(card)
    card = GameDeck.drawCard()
    dealer.drawCard(card)
    card = GameDeck.drawCard()
    player.drawCard(card)
    card = GameDeck.drawCard()
    dealer.drawCard(card)

    #Player's Go
    print("Player, it's your go.")
    player.showHand()
    cardsInHand = player.returnHand()
    handScore = scorer.countScore(cardsInHand)
    if handScore == 21:
        pass
    else:
        while handScore < 22:
            print(f"Player, the value of your hand is { handScore }.")
            print("Would you like to hit?")
            decision = input("Insert Y for Hit, or N for Stick: ")
            if decision == "Y":
                    card = GameDeck.drawCard()
                    player.drawCard(card)
                    cardsInHand = player.returnHand()
                    player.showHand()
                    handScore = scorer.countScore(cardsInHand)
            elif decision == "N":
                break
            else:
                print("Invalid Input.")
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
    print("Dealer, it's your go.")
    dealer.showHand()
    cardsInHand = dealer.returnHand()
    handScore = scorer.countScore(cardsInHand)
    if handScore == 21:
        pass
    else:
        while handScore < 22:
            if handScore < 16:
                print("Dealer hits.")
                card = GameDeck.drawCard()
                dealer.drawCard(card)
                cardsInHand = dealer.returnHand()
                player.showHand()
                handScore = scorer.countScore(cardsInHand)
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