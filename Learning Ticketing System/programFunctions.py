import asyncio

async def intro():
    print('Hello World.')
    await asyncio.sleep(0.25)
    print('Welcome to the Learning Ticketing System.')
    await asyncio.sleep(0.25)

async def options():
    print('OPTIONS MENU')
    await asyncio.sleep(0.25)
    print('Please select an option:')
    await asyncio.sleep(0.25)
    print('1. Open Ticket.')
    await asyncio.sleep(0.25)
    print('2. Close Ticket.')
    # await asyncio.sleep(0.25)
    # print('3. Update Ticket.')
    # await asyncio.sleep(0.25)
    # print('4. Edit Ticket.')
    # await asyncio.sleep(0.25)
    # print('5. Reopen Ticket.')
    await asyncio.sleep(0.25)
    print('6. Show Tickets.')
    await asyncio.sleep(0.25)
    print('0. Close System.')
    await asyncio.sleep(0.25)
    choice = int(input("Type an integer 0 - 5: "))
    return choice

async def returnToOptions():
    await asyncio.sleep(0.25)
    print("Work flow complete. Returning to OPTIONS MENU.")
    await asyncio.sleep(0.25)