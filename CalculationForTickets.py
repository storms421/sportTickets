# This function will take payments from the customer to purchase tickets
def ticket_payment(total_price):

    while True:
        print("Your total will be " + str(total_price))

        payment_code = input("Please enter your zip code to pay or 0 to cancel: ")

        # If 0 is entered, cancel payment and return to menu
        if payment_code.isdigit() and int(payment_code) == 0:
            print("\nTransaction Cancelled")
            break
        # If 5-digit zip code is entered, accept and go to receipt function
        elif payment_code.isdigit() and len(payment_code) == 5:
            take_receipt()
            break
        # If user inputs incorrectly, loop
        else:
            print("Invalid Input")


# This function will see if the user would like their receipt or not!
def take_receipt():
    while True:
        print("Thank you for your purchase!")
        receipt = input("Would you like your receipt? \n(1) Yes \n(2) No\n")

        # If receipt is wanted, print
        if receipt.isdigit() and int(receipt) == 1:
            print("Receipt")
            print("Enjoy the game!")
            break
        # If receipt is not wanted, directly to end message
        elif receipt.isdigit() and int(receipt) == 2:
            print("Enjoy the game!")
            break
        # If invalid response, loop
        else:
            print("Invalid Input")


