import CalculationForTickets


def denver_nuggets_tickets(nuggets_seats, nuggets_prices):

    while True:
        print("\nWelcome to the Denver Nuggets ticket selection!")
        for index in range(len(nuggets_seats)):
            print("(" + str(index + 1) + ") " + nuggets_seats[index] + " <- " + str(nuggets_prices[index]))

        seat_selection = input("Which seat level would you like to purchase or 0 to go back?: ")

        if int(seat_selection) == 0:
            break
        elif int(seat_selection) <= 3 and seat_selection.isdigit():
            print("You have selected " + str(nuggets_seats[int(seat_selection) - 1]))
            correct_seats(nuggets_seats, seat_selection)
            total_tickets = input("How many tickets would you like to purchase? (Max 4): ")
            if int(total_tickets) <= 4:
                print("Great!")
                total = nuggets_prices[int(seat_selection) - 1] * int(total_tickets)
                CalculationForTickets.ticket_payment(total)
                break
        else:
            print("Invalid Input")


def correct_seats(seats, index):
    while True:
        print("You have selected " + str(seats[int(index) - 1]))
        confirm = input("Is this correct? \n(1) Yes \n(2) No\n")
        if confirm.isdigit() and int(confirm) == 1:
            break
        elif confirm.isdigit() and int(confirm) == 2:
            break
        else:
            print("Invalid Input")
