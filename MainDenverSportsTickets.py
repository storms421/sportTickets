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
team_selected = ""

# Loops until admin/customer wants to leave
while True:
    print("Welcome to Colorado sports ticket service!")
    customer_read = CalculationForTickets.yes_or_no("Are you a customer? \n(1) Yes \n(2) No\n")

    # If customer, go to purchase tickets for team
    if int(customer_read) == 1:
        print("")
        team_selected = CustomerAccess.select_team(teams_data)  # Goes to Customer file
        seat_selected = CustomerAccess.seat_selection(team_selected, teams_data)
        package_selected = CustomerAccess.ticket_quantity(seat_selected, seat_packages)
        is_paid = CalculationForTickets.ticket_payment(package_selected, seat_selected, teams_data, team_selected)

        if is_paid is not None:
            CalculationForTickets.take_receipt(package_selected, seat_selected, teams_data, team_selected)
            
    # If admin, go to admin to update information
    elif int(customer_read) == 2:
        print("")
        gained_access = AdminAccess.admin_access(password)  # Goes to Admin file

        if gained_access == 1:
            AdminAccess.menu()

    # Checks to see if program ends
    escape = CalculationForTickets.yes_or_no("\nAre we ready to logout? \n(1) Yes \n(2) No\n")
    print("")
    # If yes is selected, exit program
    if escape == 1:
        break
