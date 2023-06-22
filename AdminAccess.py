import AdditionalFunctionSportTickets
import CalculationForTickets


# This function will check if user is allowed access to admin profile
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


# This function will display the admin menu and take selected option from menu and return
def menu(admin_menu):

    while True:
        print("\nWelcome, Admin!")
        for position, index in enumerate(range(len(admin_menu))):  # Displays menu options
            print("(" + str(position + 1) + ") " + admin_menu[index])
        admin_menu_selection = input("What would you like to do?: ")

        # Take in valid menu selection
        valid_menu_selection = AdditionalFunctionSportTickets.integer_validation(admin_menu_selection, admin_menu)

        # Return valid selection
        if valid_menu_selection is not None:
            return valid_menu_selection


# This function will find the teams with a sale and edit their prices
def sales_event(teams_info):
    while True:
        print("\nWelcome to Sales Event Editor!")
        for index, team_names in enumerate(teams_info.keys()):  # Displays teams
            print("(" + str(index + 1) + ") " + team_names)
        team_selected = input("Which team has a sale going on or 0 to exit?: ")

        # Return to menu
        if team_selected == "0":
            break

        # Checks for valid input
        valid_team_selection = AdditionalFunctionSportTickets.integer_validation(team_selected, teams_info)

        # Once input is valid, ask for sales percentage
        if valid_team_selection is not None:
            sales_percentage = CalculationForTickets.percentage_calculator()  # Calculates percentage for sales

            team_name = list(teams_info.keys())[valid_team_selection - 1]  # Retrieves team name
            prices = teams_info[team_name]["Prices"]  # Retrieves price list
            seats = teams_info[team_name]["Seats"]  # Retrieves seat list
            # Loops through, calculates price
            updated_prices = [round(price - (price * sales_percentage), 2) for price in prices]
            teams_info[team_name]["Prices"] = updated_prices  # Updates prices in team dictionary

            # Will need to figure out how to round here *********
            print("\nThe " + team_name + " got a sale of " + str(sales_percentage * 100) + "% off tickets:")
            print("******************************************")
            # Loop through the seating's and new prices offered for selected team
            for position, index in enumerate(range(len(seats))):
                print("\t(" + str(position + 1) + ") " + seats[index] + " -> " + str(updated_prices[index]))
            print("******************************************")
            print("Prices have been updated successfully...\n")

            # Leave to menu if answering No
            leave = AdditionalFunctionSportTickets.yes_or_no("Any more sales? \n(1) Yes \n(2) No\n")
            if leave == 2:
                break


def charity_event(teams_info):
    print("Charity Event!")


def seating_name_change(teams_info):
    print("Change Seating Names!")


def change_package_deals(teams_info):
    print("Change Package Deals!")
