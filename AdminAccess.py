# Will improve this later
def admin_access(password):
    i = 0

    # While you have 3 tries, enter the password
    while i <= 2:
        entered_password = input("Please enter the password: ")
        # If password is correct, move on
        if password == entered_password:
            return 1
        # If password is wrong, increment attempt counter
        else:
            print("Password is incorrect!")
            i += 1


def menu():
    print("\nWelcome, Admin!"
          "\n\t(1) Add Sales Event"
          "\n\t(2) Add Charity Event"
          "\n\t(3) Change Seating Names"
          "\n\t(4) Exit"
          "\nWhat would you like to do?: ")


def sales_event():
    print("Sales Event!")


def charity_event():
    print("Charity Event!")


def seating_name_change():
    print("Change Seating Names!")
