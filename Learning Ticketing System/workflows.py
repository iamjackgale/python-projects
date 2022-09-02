import asyncio
import open
import close
import show

async def workflow(choice: int, ticketCounter: int, ticketList: list):

    #Option 1 - open
    if choice == 1:
        await asyncio.sleep(1)
        ticketNumber = ticketCounter + 1
        newTicket = open.open(ticketNumber)
        ticketList.append(newTicket)
        ticketCounter += 1
        return [ticketCounter, ticketList]

    #Option 2 - close
    if choice == 2:
        await asyncio.sleep(1)
        closeTicket = close.close()
        for n in ticketList:
            if n[0] == closeTicket:
                ticketList.pop(ticketList.index(n))
                print(f"Ticket Number #{ closeTicket } has now been closed.")
        return [ticketCounter, ticketList]

    #Option 3 - update

    #Option 4 - edit

    #Option 5 - reopen

    #Option 6 - show
    if choice == 6:
        await asyncio.sleep(1)
        show.show(ticketList)
        return [ticketCounter, ticketList]