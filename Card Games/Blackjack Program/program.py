import asyncio
import intro
import blackjack

if __name__ == "__main__":
    asyncio.run(intro.intro())
    
    breaker = False
    while breaker == False:
        choice = input("Would you like to play Blackjack? Y/N: ")
        if choice == "Y":
            blackjack.blackjack()
        else:
            print("Thank you for playing. Goodbye!")
            breaker = True