# This function will take payments from the customer to purchase tickets
def ticket_payment(total_price, team_seats_name, total_tickets_to_purchase, nuggets_team_name_written):
    while True:
        print("Your total will be " + str(total_price))

        payment_code = input("Please enter your zip code to pay or 0 to cancel: ")

        # If 0 is entered, cancel payment and return to menu
        if payment_code.isdigit() and int(payment_code) == 0:
            print("\nTransaction Cancelled")
            break
        # If 5-digit zip code is entered, accept and go to receipt function
        elif payment_code.isdigit() and len(payment_code) == 5:
            take_receipt(team_seats_name, total_tickets_to_purchase, total_price, nuggets_team_name_written)
            break
        # If user inputs incorrectly, loop
        else:
            print("Invalid Input")


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
