#Card deck module functionality sample program, designed to allow users to test the various functions of the deck.py module.

from deck import Deck
import time

print("Hello. Welcome to the deck.py functionality sample program.")
choice = 1

while choice > 0:

    #Options Menu    
    print("Please select an option to proceed:")
    print("1. New Deck")
    print("2. Show Current Deck")
    print("3. Shuffle Deck")
    print("4. Draw a Card")
    print("5. Return a Card to the Top of the Deck")
    print("6. Return a Card to the Bottom of the Deck")
    print("7. Return a Card to a Specific Position in the Deck")
    print("8. Return a Card to a Random Position in the Deck")
    print("9. Display the Deck Dictionary")
    print("0. Exit")
    choice = int(input("Type the integer 0 - 9:"))

    #Option 1
    if choice == 1:
        print(TestDeck.newDeck())
        time.sleep(2)
    
    #Option 2
    if choice == 2:
        print(TestDeck.showDeck())
        time.sleep(2)

    #Option 3
    if choice == 3:
        print(TestDeck.shuffleDeck())
        time.sleep(2)

    #Option 4
    if choice == 4:
        print(TestDeck.drawCard())
        time.sleep(2)

    #Option 5
    if choice == 5:
        card = str(input("Input your chosen card:"))
        print(TestDeck.returnCardTop(card))
        time.sleep(2)

    #Option 6
    if choice == 6:
        card = str(input("Input your chosen card:"))
        print(TestDeck.returnCardBottom(card))
        time.sleep(2)

    #Option 7
    if choice == 7:
        card = str(input("Input your chosen card:"))
        position = int(input("Input your chosen position as an integer between 1 and the total number of cards in the deck: "))
        print(TestDeck.returnCardSpecific(card, position))
        time.sleep(2)

    #Option8
    if choice == 8:
        card = str(input("Input your chosen card:"))
        print(TestDeck.returnCardRandom(card))
        time.sleep(2)

    #Option 9
    if choice == 9:
        print(TestDeck.deckDict())
        print(TestDeck.dict)
        time.sleep(2)

    #Option 0
    elif choice == 0:
        print("Thank you for trying the deck.py functionality sample program.")
        break