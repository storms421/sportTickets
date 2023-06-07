import AdminAccess
import CustomerAccess

teams = ["Denver Broncos", "Denver Nuggets", "Colorado Avalanche", "Colorado Rapids", "Colorado Rockies"]
seats = ["Courtside", "Mid Seats", "Upper Seats"]
prices = [150.00, 100.00, 50.00]
password = "7215"
outer_escape = True

# Loops until admin/customer wants to leave
while outer_escape:
    print("Welcome to Colorado sports ticket service!")
    customer_read = input("Are you a customer? \n(1)Yes \n(2)No\n")

    # If customer, go to purchase tickets for team
    if int(customer_read) == 1:
        print("")
        CustomerAccess.customer_access(teams, seats, prices)  # Goes to customer file
    # If admin, go to admin to update information
    elif int(customer_read) == 2:
        print("")
        AdminAccess.admin_access(password)  # Goes to Admin file
    else:
        print("Invalid Input")

    # Inner loop to for escaping program
    inner_escape = True
    while inner_escape:
        leave = input("\nAre we ready to logout? \n(1)Yes \n(2)No\n")

        if int(leave) == 1:
            inner_escape = False  # Breaks inner loop since valid option
            outer_escape = False
        elif int(leave) == 2:
            inner_escape = False  # Breaks inner loop since valid option
            outer_escape = True
        else:
            print("Invalid Input")




