import AdminAccess
import CustomerAccess
import CalculationForTickets

# Start of teams dictionary
teams_data = {

    "Denver Broncos": {
        "Seats": ["Home Side", "Visitor Side", "Southside Field Goal", "Northside Field Goal"],
        "Prices": [200.00, 100.00, 50.00, 50.00]
    },  # End of Denver Broncos

    "Denver Nuggets": {
        "Seats": ["Courtside", "Mid Seats", "Upper Seats"],
        "Prices": [150.00, 100.00, 50.00]
    },  # End of Denver Nuggets

    "Colorado Avalanches": {
        "Seats": ["Team Side"],
        "Prices": [100.00]
    },  # End of Colorado Avalanches

    "Colorado Rapids": {
        "Seats": ["Goalside"],
        "Prices": [50.00]
    },  # End of Colorado Rapids

    "Colorado Rockies": {
        "Seats": [],
        "Prices": []
    }  # End of Colorado Rockies

}  # End of dictionary

seat_packages = ["Single Ticket", "Double Ticket", "Triple Ticket", "Quadruple Ticket"]
password = "7215"
outer_escape = True
team_selected = ""

# Loops until admin/customer wants to leave
while outer_escape:
    print("Welcome to Colorado sports ticket service!")
    customer_read = input("Are you a customer? \n(1) Yes \n(2) No\n")

    # If customer, go to purchase tickets for team
    if int(customer_read) == 1:
        print("")
        team_selected = CustomerAccess.select_team(teams_data)  # Goes to Customer file
        seat_selected = CustomerAccess.seat_selection(team_selected, teams_data)
        package_selected = CustomerAccess.ticket_quantity(seat_selected, seat_packages)
        is_paid = CalculationForTickets.ticket_payment(package_selected, seat_selected, teams_data, team_selected)

        if is_paid is not None:
            print("Receipt Function Here")
            
    # If admin, go to admin to update information
    elif int(customer_read) == 2:
        print("")
        AdminAccess.admin_access(password)  # Goes to Admin file
    else:
        print("Invalid Input")

    # Inner loop to for escaping program
    inner_escape = True
    while inner_escape:
        leave = input("\nAre we ready to logout? \n(1) Yes \n(2) No\n")

        if int(leave) == 1:
            inner_escape = False  # Breaks inner loop since valid option
            outer_escape = False
        elif int(leave) == 2:
            inner_escape = False  # Breaks inner loop since valid option
            outer_escape = True
        else:
            print("Invalid Input")
