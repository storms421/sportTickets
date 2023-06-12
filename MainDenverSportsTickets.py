import AdminAccess
import CustomerAccess

# Come back to simplify
teams = ["Denver Broncos", "Denver Nuggets", "Colorado Avalanche", "Colorado Rapids", "Colorado Rockies"]

# Start of teams dictionary
teams_data = {"Denver Broncos": {
    "Seats": ["Home Side", "Visitor Side", "Southside Field Goal", "Northside Field Goal"],
    "Prices": {
        "Home Side": 200.00,
        "Visitor Side": 100.00,
        "Southside Field Goal": 50.00,
        "Northside Field Goal": 50.00
    }
},  # End of Denver Broncos

    "Denver Nuggets": {
        "Seats": ["Courtside", "Mid Seats", "Upper Seats"],
        "Prices": {
            "Courtside": 150.00,
            "Mid Seats": 100.00,
            "Upper Seats": 50.00
        }

    }  # End of Denver Nuggets

}  # End of dictionary

password = "7215"
outer_escape = True
team_selected = ""

# Loops until admin/customer wants to leave
while outer_escape:
    print("Welcome to Colorado sports ticket service!")
    customer_read = input("Are you a customer? \n(1)Yes \n(2)No\n")

    # If customer, go to purchase tickets for team
    if int(customer_read) == 1:
        print("")
        team_selected = CustomerAccess.select_team(teams_data)  # Goes to Customer file
        print(team_selected)
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
