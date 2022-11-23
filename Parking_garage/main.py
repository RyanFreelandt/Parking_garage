class Parking():
    def __init__(self, tickets, pay, leave, parkingSpaces, currentTicket):
        self.tickets = tickets
        self.pay = pay
        self.leave = leave
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket

    def takeTicket(self):
        tickets = [1,2,3,4,5,6,7,8,9,10]
        print(f"Please take a parking ticket.")
        tickets = tickets.pop()
        parkingSpaces = parkingSpaces.pop()
        
    def payForParking(self):
        input(int("Enter ticket amount: "))
        print("Your ticket has been paid, you have 15 minutes to leave.")
        print("Thank you, have a nice day!")
        parkingSpaces = parkingSpaces.append()
        tickets = tickets.append()
