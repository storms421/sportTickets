# Will improve this later
def admin_access(password):
    i = 0

    # While you have 3 tries, enter the password
    while i <= 3:
        entered_password = input("Please enter the password: ")
        # If password is correct, move on
        if password == entered_password:
            sales_check()
            i = 4  # Breaks loop
        # If password is wrong, increment attempt counter
        else:
            print("Password is incorrect!")
            i += 1


def sales_check():
    print("Welcome, Admin!")
