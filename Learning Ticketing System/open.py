def open(ticketNumber: int): #ticket numbering is counted in main file
    newTicket = []
    newTicket.append(ticketNumber)
    name = str(input("Type the name of your ticket: "))
    newTicket.append(name)
    print(f"Ticket '{name}' created.")
    return newTicket