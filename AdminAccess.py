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
def sales_event(teams_info, package_deals):
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
            # Calculates percentage for sales
            sales_percentage = CalculationForTickets.percentage_valid("How much are the "
                                                                      "tickets off today? (Enter an integer of 1-99): ")

            team_name = list(teams_info.keys())[valid_team_selection - 1]  # Retrieves team name
            prices = teams_info[team_name]["Prices"]  # Retrieves price list
            seats = teams_info[team_name]["Seats"]  # Retrieves seat list
            # Loops through, calculates price
            updated_prices = [round(price - (price * sales_percentage), 2) for price in prices]
            teams_info[team_name]["Prices"] = updated_prices  # Updates prices in team dictionary
            teams_info[team_name]["Percentage"] = sales_percentage  # Updates the dictionary with the sales percentage
            # Will need to figure out how to round here *********
            print("\nThe " + team_name + " got a sale of {:.0f}".format((sales_percentage * 100)) + "% off tickets:")
            print("******************************************")
            # Loop through the seating's and new prices offered for selected team
            for position, index in enumerate(range(len(seats))):
                print("\t(" + str(position + 1) + ") " + seats[index] + " -> {:.2f}".format(updated_prices[index]))
            print("******************************************")
            print("Prices have been updated successfully...\n")

            # Leave to menu if answering No
            leave = AdditionalFunctionSportTickets.yes_or_no("Any more sales? \n(1) Yes \n(2) No\n")
            if leave == 2:
                break


# This function will grab the percentage going to charity
def charity_event(teams_info, package_deals):
    while True:
        print("\nWelcome to Charity Event Editor!")
        for index, team_names in enumerate(teams_info.keys()):  # Displays teams
            print("(" + str(index + 1) + ") " + team_names)
        team_selected = input("Which team has a charity going on or 0 to exit?: ")

        # Return to menu
        if team_selected == "0":
            break

        # Checks for valid input
        valid_team_selection = AdditionalFunctionSportTickets.integer_validation(team_selected, teams_info)

        # Once input is valid, ask for charity percentage
        if valid_team_selection is not None:
            # Calculates percentage for charity
            charity_percentage = CalculationForTickets.percentage_valid("What percentage of the tickets are going to "
                                                                        "charity today? (Enter an integer of 1-99): ")

            team_name = list(teams_info.keys())[valid_team_selection - 1]  # Retrieves team name
            teams_info[team_name]["Charity"] = charity_percentage  # Updates the dictionary with the charity percentage

            print("\nCharity event has been successfully added to the " + team_name)
            print("The customer's total sale will have {:.0f}".format((charity_percentage * 100)) + "% go to charity\n")

            # Leave to menu if answering No
            leave = AdditionalFunctionSportTickets.yes_or_no("Any more charity events? \n(1) Yes \n(2) No\n")
            if leave == 2:
                break


# This function will change the seat names (rename)
def seating_name_change(teams_info, package_deals):
    while True:
        print("\nWelcome to the Seat Name Editor!")
        # Lists sport teams
        for index, team_names in enumerate(teams_info.keys()):
            print("(" + str(index + 1) + ") " + team_names)

        team_selected = input("Which team needs a seat name change or 0 to go back?: ")

        # Return to admin menu
        if team_selected == "0":
            return

        # Check for valid input by admin
        team_index = AdditionalFunctionSportTickets.integer_validation(team_selected, teams_info)

        if team_index is not None:
            selected_team_name = list(teams_info.keys())[team_index - 1]  # Convert dictionary keys into list, stores it
            team_details = teams_info[selected_team_name]  # Retrieves appropriate seats and prices and stores it
            seats = team_details["Seats"]  # Pulls seats of selected sports team, stores it

            while True:
                print("\nHere is the list of seats for the " + selected_team_name + ":")
                # Lists selected sports teams seating
                for index, seat_names in enumerate(seats):
                    print("(" + str(index + 1) + ") " + seat_names)

                seat_selected = input("Which seat would you like to rename or 0 to go back?: ")

                # Return to team selection
                if seat_selected == "0":
                    break

                # Check for valid input by admin
                seat_index = AdditionalFunctionSportTickets.integer_validation(seat_selected, seats)

                # If valid, move to rename process
                if seat_index is not None:
                    confirmed_rename = rename_seat(seat_index, seats)
                    # Goes back
                    if confirmed_rename == 1:
                        break


# This function allows admin to rename seats and then confirm if it's correct
def rename_seat(seat_index_valid, teams_seats):
    new_seat_name = input("\nPlease enter the new seating name: ")

    is_correct = AdditionalFunctionSportTickets.yes_or_no("\nIs the seat name, " + new_seat_name +
                                                          ", correct?: \n(1) Yes \n(2) No\n")

    # If the seat name is correct, go back to start of seat editor
    if is_correct == 1:
        teams_seats[seat_index_valid - 1] = new_seat_name  # Replaces old seat with new seat
        print("The renamed seat has successfully been updated...")
        for index, seat_names in enumerate(teams_seats):  # Displays seats with newly named seat
            print("(" + str(index + 1) + ") " + seat_names)
        return 1  # Used to return to start of seat editor


# This function will change the package deals (add)
def change_package_deals(teams_info, package_deals):
    print("\nWelcome to Package Deals Editor!")

    # Loop until admin is done entering in new package names
    while True:
        package_name = input("What would you like to name the new package deal or 0 to exit?: ")

        # If package is 0, exit
        if package_name == "0":
            return
        # If new name, ask if it's correct
        else:
            is_correct = AdditionalFunctionSportTickets.yes_or_no("Is the name package, "
                                                                  + package_name + ", correct? \n(1) Yes \n(2) No\n")
            # If name is correct, add to package list
            if is_correct == 1:
                package_deals.append(package_name)  # Adds to package list
                print("Package deal has successfully been added...")
                for position, index in enumerate(range(len(package_deals))):  # Displays newly added package
                    print("(" + str(position + 1) + ") " + package_deals[index])


# This function will let admin change specific seating prices
def change_seating_prices(teams_info, package_deals):
    seat_selected = 0  # Initializing (needed to use outside of loop as well)
    while True:
        print("\nWelcome to Seating Price Editor!")
        # Lists sport teams
        for index, team_names in enumerate(teams_info.keys()):
            print("(" + str(index + 1) + ") " + team_names)

        team_selected = input("Which team needs seat price change or 0 to go back?: ")

        # Return to admin menu
        if team_selected == "0":
            return

        # Check for valid input by admin
        team_index = AdditionalFunctionSportTickets.integer_validation(team_selected, teams_info)

        if team_index is not None:
            selected_team_name = list(teams_info.keys())[team_index - 1]  # Convert dictionary keys into list, stores it
            team_details = teams_info[selected_team_name]  # Retrieves appropriate seats and prices and stores it
            seats = team_details["Seats"]  # Pulls seats of selected sports team, stores it
            prices = team_details["Prices"]  # Retrieves price list

            while True:
                print("\nHere is the list of seats for the " + selected_team_name + ":")
                # Lists selected sports teams seating and prices
                for index, seat_names in enumerate(seats):
                    print("(" + str(index + 1) + ") " + seat_names + " -> {:.2f}".format(prices[index]))

                seat_selected = input("Which seat will need a price change or 0 to go back?: ")

                # Return to team selection
                if seat_selected == "0":
                    break

                # Check for valid input by admin
                seat_index = AdditionalFunctionSportTickets.integer_validation(seat_selected, seats)

                # If valid, move to price change process
                if seat_index is not None:
                    is_price_changed = seating_price_change_update(seats, seat_index, prices, teams_info,
                                                                   selected_team_name)
                    # If price was updated, break
                    if is_price_changed == 1:
                        break

        # If user updated a price, ask if they want to modify more
        if seat_selected != "0":
            # Check for if admin wants to modify more
            exit_to_menu = AdditionalFunctionSportTickets.yes_or_no("\nWould you like to modify another "
                                                                    "seating price? \n(1) Yes \n(2) No\n")
            # If admin is done, return to menu
            if int(exit_to_menu) == 2:
                break


# This function will do the input, confirming, and updating of the new seating price
def seating_price_change_update(seats_inner, seat_index_inner, prices_inner, teams_info_inner,
                                selected_team_name_inner):
    while True:
        price_update = input("Enter the new price for the seat " + seats_inner[seat_index_inner - 1] +
                             " or 0 to go back: ")

        # Return to team selection
        if price_update == "0":
            break

        if price_update.isdigit():
            price_update = int(price_update)
            if price_update > 0:  # If price is greater than 0, ask to confirm price
                is_confirmed = AdditionalFunctionSportTickets.yes_or_no(
                    "The price $" + "{:.2f}".format(prices_inner[seat_index_inner - 1])
                    + " for the seat " + seats_inner[seat_index_inner - 1] +
                    " will be updated to the price $" +
                    "{:.2f}".format(price_update) +
                    ". Is this correct? \n(1) Yes \n(2) No\n")

                # If seat is confirmed, update
                if int(is_confirmed) == 1:
                    prices_inner[seat_index_inner - 1] = price_update  # Updates the price in the index selected
                    teams_info_inner[selected_team_name_inner]["Prices"] = prices_inner  # Updates the price in dict.
                    print("The seating price has successfully been updated...")
                    # Displays all seats with new seating price updated
                    for index, seat_names in enumerate(seats_inner):
                        print("(" + str(index + 1) + ") " + seat_names + " -> {:.2f}".format(prices_inner[index]))
                    return 1
            else:
                print("Invalid Input")
        else:
            print("Input must be a number!")
