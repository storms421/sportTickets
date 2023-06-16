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
                return None
            elif len(str(payment_code)) == 5:
                return payment_code
            else:
                print("Invalid Input")
        else:
            print("Input must be a number!")


# This function will see if the user would like their receipt or not!
def take_receipt(teams_seats_name_deep, total_tickets_to_purchase_deep, total_price_deep, nuggets_team_name_deep):
    while True:
        print("Thank you for your purchase!")
        receipt = input("Would you like your receipt? \n(1) Yes \n(2) No\n")

        # If receipt is wanted, print
        if receipt.isdigit() and int(receipt) == 1:
            receipt_for_customer(teams_seats_name_deep, total_tickets_to_purchase_deep, total_price_deep,
                                 nuggets_team_name_deep)
            print("Enjoy the game!")
            break
        # If receipt is not wanted, directly to end message
        elif receipt.isdigit() and int(receipt) == 2:
            print("Enjoy the game!")
            break
        # If invalid response, loop
        else:
            print("Invalid Input")


def receipt_for_customer(teams_seats_name_deeper, total_tickets_to_purchase_deeper, total_price_deeper,
                         nuggets_team_name_deeper):
    print("Receipt"
          "\n\tTeam: " + nuggets_team_name_deeper +
          "\n\tSeats: " + str(teams_seats_name_deeper) +
          "\n\tTicket Count: " + str(total_tickets_to_purchase_deeper) +
          "\n\tTotal: $" + str(total_price_deeper))
