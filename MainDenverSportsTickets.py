import AdminAccess
import CustomerAccess
import CalculationForTickets
import AdditionalFunctionSportTickets

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

}  # End of teams_data dictionary


# Start of menu_functions
# This dictionary will allow for functions to be called based on user selection (simplified if/elif/else)
menu_functions = {
    1: AdminAccess.sales_event,
    2: AdminAccess.charity_event,
    3: AdminAccess.seating_name_change,
    4: AdminAccess.change_package_deals
}  # End of menu_functions dictionary

seat_packages = ["Single Ticket", "Double Ticket", "Triple Ticket", "Quadruple Ticket"]
admin_options = ["Add Sales Event", "Add Charity Event", "Change Seating Names", "Change Package Deals", "Exit"]
password = "7215"
team_selected = ""

# Loops until admin/customer wants to leave
while True:
    print("Welcome to Colorado sports ticket service!")
    customer_read = AdditionalFunctionSportTickets.yes_or_no("Are you a customer? \n(1) Yes \n(2) No\n")

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

        while True:
            if gained_access == 1:
                menu_selection = AdminAccess.menu(admin_options)

                # If the last option is picked (always exit), then leave admin section
                if menu_selection == len(admin_options):
                    break

                # Grab selected function and store it
                selected_option = menu_functions.get(menu_selection)
                # Find menu option and go to function
                if selected_option:
                    selected_option()

    # Checks to see if program ends
    escape = AdditionalFunctionSportTickets.yes_or_no("\nAre we ready to logout? \n(1) Yes \n(2) No\n")
    print("")
    # If yes is selected, exit program
    if escape == 1:
        break
