import AdditionalFunctionSportTickets


# This function will take payments from the customer to purchase tickets
def ticket_payment(package_ticket, seat_section_selected, teams_info, team_index):
    selected_team = list(teams_info.keys())[team_index - 1]  # Converts dictionary keys into a list, stores it
    team_details = teams_info[selected_team]  # Retrieves appropriate seats and prices and stores it
    seat_prices = team_details["Prices"][seat_section_selected - 1]  # Retrieves seat price based on selected seat
    total_price = seat_prices * package_ticket  # Calculates the total

    # While user inputs info, loop through
    while True:
        print("\nYour total will be $" + str(total_price))

        payment_code = input("Please enter your zip code to pay or 0 to cancel transaction: ")

        if payment_code.isdigit():
            if int(payment_code) == 0:
                print("\n***Transaction Cancelled***")
                return None
            elif len(str(payment_code)) == 5:
                return payment_code
            else:
                print("Invalid Input")
        else:
            print("Input must be a number!")


# This function will see if the user would like their receipt or not!
def take_receipt(package_ticket, seat_section_selected, teams_info, team_index):
    selected_team = list(teams_info.keys())[team_index - 1]  # Converts dictionary keys into a list, stores it
    team_details = teams_info[selected_team]  # Retrieves appropriate seats and prices and stores it
    seat_prices = team_details["Prices"][seat_section_selected - 1]  # Retrieves seat price based on selected seat
    seat_location = team_details["Seats"][seat_section_selected - 1]  # Retrieves seat price based on selected seat
    total_price = seat_prices * package_ticket  # Calculates the total

    print("\nThank you for your purchase!")
    receipt = AdditionalFunctionSportTickets.yes_or_no("Would you like your receipt? \n(1) Yes \n(2) No\n")

    # If user wants receipt, print it
    if receipt == 1:
        print("Receipt"
              "\n\tTeam: " + selected_team +
              "\n\tSeats: " + seat_location +
              "\n\tTotal: $" + str(total_price))
    else:
        print("Enjoy the game!")


def percentage_calculator():
    while True:
        sales_percentage = input("How much are the tickets off today? (Enter an integer of 1-99): ")

        if sales_percentage.isdigit():
            sales_percentage = int(sales_percentage) / 100
            if 0.01 <= sales_percentage <= 0.99:
                return sales_percentage
            else:
                print("Input is out of range!")
        else:
            print("Input is not an integer!")

