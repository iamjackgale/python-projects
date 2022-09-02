import asyncio
import programFunctions
import workflows

ticketCounter = 0
ticketList = []

if __name__ == "__main__":
    asyncio.run(programFunctions.intro())
    circuitbreaker = False
    while circuitbreaker == False:
        choice = asyncio.run(programFunctions.options())
        if choice == 0:
            print("Thank you for visiting.")
            circuitbreaker = True
        else:
            output = asyncio.run(workflows.workflow(choice, ticketCounter, ticketList))
            ticketCounter = output[0]
            ticketList = output [1]
            asyncio.run(programFunctions.returnToOptions())