import AdditionalFunctionSportTickets
from collections import OrderedDict


# This function will add a team to the dictionary
def add_team(teams_info):
    while True:
        new_team = input("\nEnter the new team name or 0 to go back: ")

        # If user enters 0, go back to submenu
        if new_team == "0":
            break

        # Confirm team name is correct
        confirmed_add = AdditionalFunctionSportTickets.yes_or_no("\nBelow is the new team name\n\t" + new_team +
                                                                 "\nIs this correct?: \n(1) Yes \n(2) No\n")

        # If confirmed, add team with seat and price sections
        if confirmed_add == 1:
            teams_info[new_team] = {"Seats": [], "Prices": []}

            print("Let's add some seat and pricing options for this team.\n")
            # Loop for valid input
            while True:
                seat_count = input("Enter how many seats will we be added to the new team or 0 to exit: ")

                if seat_count == "0":
                    return 1

                # Get valid amount of seats to add
                if seat_count.isdigit() and 0 < int(seat_count) <= 10:
                    team_details = teams_info[new_team]  # Retrieves appropriate seats and prices and store it
                    seats = team_details["Seats"]  # Pulls seats of selected sports team, stores it
                    prices = team_details["Prices"]

                    # Reuses function to get a set amount of seats and their prices to add to new team
                    add_seats(team_details, seats, prices, int(seat_count))

                    # Return to ask if more to modify
                    return 1

                else:
                    print("Invalid Input. Try again.\n")


# This function will remove a team from the dictionary
def remove_team(teams_info):
    while True:
        print("\nHere is the list of teams currently in the system:")
        for index, team_name in enumerate(teams_info.keys()):  # Loops through teams
            print("(" + str(index + 1) + ") " + team_name)
        selected_team_delete = input("Which sports team would you like to delete or 0 to go back: ")

        if int(selected_team_delete) == 0:
            break

        # Validates Selection
        selected_team_delete = AdditionalFunctionSportTickets.integer_validation(selected_team_delete, teams_info)

        if selected_team_delete is not None:
            team_names = list(teams_info.keys())  # Stores teams as a list
            name_of_team = team_names[selected_team_delete - 1]  # Grabs selected team
            confirmed_deletion = AdditionalFunctionSportTickets.yes_or_no("\nAre you sure you want to delete the team, "
                                                                          + name_of_team + "?: \n(1) Yes \n(2) No\n")

            # If confirmed, delete team
            if confirmed_deletion == 1:
                del teams_info[name_of_team]  # Deletes team and all its data
                print("\nThe team has successfully been deleted...")
                for index, team_name in enumerate(teams_info.keys()):  # Loops through updated teams list
                    print("(" + str(index + 1) + ") " + team_name)
                return 1


# This function will rename a team from the dictionary
def rename_team(teams_info):
    while True:
        print("\nHere is the list of teams currently in the system:")
        for index, team_name in enumerate(teams_info.keys()):  # Loops through teams
            print("(" + str(index + 1) + ") " + team_name)
        selected_team_rename = input("Which sports team would you like to rename or 0 to go back: ")

        # Goes back to submenu
        if int(selected_team_rename) == 0:
            break

        # Validates selection
        selected_team_rename = AdditionalFunctionSportTickets.integer_validation(selected_team_rename, teams_info)

        if selected_team_rename is not None:
            new_team_name = input("Please enter the new team name: ")
            team_names = list(teams_info.keys())  # Stores teams as a list
            old_team_name = team_names[selected_team_rename - 1]  # Grabs selected team
            confirmed_rename = AdditionalFunctionSportTickets.yes_or_no("\nAre you sure you want to rename the team "
                                                                        "from " + old_team_name + " to " +
                                                                        new_team_name + "?: \n(1) Yes \n(2) No\n")

            # If confirmed, rename team
            if confirmed_rename == 1:
                teams_info_ordered = OrderedDict()  # Creates ordered dictionary
                for team_name, team_data in teams_info.items():  # Loops through existing teams for comparison
                    if team_name == old_team_name:  # If team to rename matches in dictionary, rename
                        teams_info_ordered[new_team_name] = team_data  # Adds renamed team to old teams "index"
                    else:
                        teams_info_ordered[team_name] = team_data  # Not matches, adds that team as is

                teams_info.clear()  # Clears original team info
                teams_info.update(teams_info_ordered)  # Updates team info dictionary with correct order

                print("\nThe team has successfully been renamed...")
                for index, team_name in enumerate(teams_info.keys()):  # Loops through updated teams list
                    print("(" + str(index + 1) + ") " + team_name)
                return 1


#######################################################################################################################
# This function will add seats to the sports team dictionary for customer
def add_seats(selected_team_name, seats, prices, amount):
    while True:
        new_seat = input("\nEnter the new seat name or 0 to stop: ")

        # If user enters 0, go back to submenu
        if new_seat == "0":
            break

        new_price = input("Enter the price for the new seat: ")
        new_price = float(new_price)  # Convert to float

        confirmed_add = AdditionalFunctionSportTickets.yes_or_no("\nBelow is the new seat and price:\n\t" + new_seat +
                                                                 " -> ${:.2f}".format(new_price) +
                                                                 "\nIs this correct?: \n(1) Yes \n(2) No\n")
        # If confirmed name and prices, add to end of dictionary list
        if confirmed_add == 1:
            seats.append(new_seat)
            prices.append(new_price)

            # Decrement seat counter for amount to add
            amount = amount - 1

            if amount < 1:
                return 1  # Returns to ask admin if they would like to modify more


# This function will remove seats from the sports team dictionary for the customers
def delete_seats(selected_team_name, seats, prices, amount):
    while True:
        print("\nHere is the list of seats for the " + selected_team_name + ":")
        # Lists selected sports teams seating
        for index, seat_names in enumerate(seats):
            print("(" + str(index + 1) + ") " + seat_names)

        seat_selected = input("Which seat would you like to remove or 0 to go back?: ")

        # Return to submenu
        if seat_selected == "0":
            break

        # Check for valid input by admin
        seat_index = AdditionalFunctionSportTickets.integer_validation(seat_selected, seats)

        # If valid, move to rename process
        if seat_index is not None:
            seat_name = seats[int(seat_index) - 1]
            confirmed_deletion = AdditionalFunctionSportTickets.yes_or_no("\nAre you sure you want to delete the seat, "
                                                                          + seat_name + "?: \n(1) Yes \n(2) No\n")

            # If the seat name is confirmed, then delete the specific seat
            if confirmed_deletion == 1:
                del seats[seat_index - 1]  # Deletes seat
                del prices[seat_index - 1]  # Deletes price

                print("\nSeat and price has successfully been deleted...")
                # Lists selected sports teams seating
                for index, seat_names in enumerate(seats):
                    print("(" + str(index + 1) + ") " + seat_names)
                return 1  # Returns to ask admin if they would like to modify more


# This function will rename the seats for the sports team dictionary for the customer
def rename_seats(selected_team_name, seats, prices, amount):
    while True:
        print("\nHere is the list of seats for the " + selected_team_name + ":")
        # Lists selected sports teams seating
        for index, seat_names in enumerate(seats):
            print("(" + str(index + 1) + ") " + seat_names)

        seat_selected = input("Which seat would you like to rename or 0 to go back?: ")

        # Return to submenu
        if seat_selected == "0":
            break

        # Check for valid input by admin
        seat_index = AdditionalFunctionSportTickets.integer_validation(seat_selected, seats)

        # If valid, move to rename process
        if seat_index is not None:
            confirmed_rename = changing_seat_name(seat_index, seats)
            # Goes back
            if confirmed_rename == 1:
                return 1  # Returns to ask admin if they would like to modify more


#######################################################################################################################
# This function will add a new package deal to the package deal list
def add_package(package_deals):
    while True:
        package_name = input("\nWhat would you like to name the new package deal or 0 to go back?: ")

        # If package is 0, exit
        if package_name == "0":
            break

        is_correct = AdditionalFunctionSportTickets.yes_or_no("\nIs the name package, "
                                                              + package_name + ", correct? \n(1) Yes \n(2) No\n")
        # If name is correct, add to package list
        if is_correct == 1:
            package_deals.append(package_name)  # Adds to package list
            print("Package deal has successfully been added...")
            for position, index in enumerate(range(len(package_deals))):  # Displays newly added package
                print("(" + str(position + 1) + ") " + package_deals[index])
            return 1


# This function will delete a package deal from the package deal list
def delete_package(package_deals):
    while True:
        print("\nBelow is the current package deals:")
        for position, index in enumerate(range(len(package_deals))):
            print("(" + str(position + 1) + ") " + package_deals[index])
        package_selected = input("Which package deal would you like to delete or 0 to go back?: ")

        if package_selected.isdigit():
            package_index = int(package_selected)

            # If package is 0, exit
            if package_index == 0:
                break

            if package_index < len(package_deals):
                confirmed_deletion = AdditionalFunctionSportTickets.yes_or_no("\nAre you sure you want to delete the "
                                                                              "package deal, " +
                                                                              package_deals[package_index - 1]
                                                                              + "? \n(1) Yes \n(2) No\n")

                if confirmed_deletion == 1:
                    del package_deals[package_index - 1]  # Deletes Package Deal
                    print("Package deal has successfully been deleted...")
                    for position, index in enumerate(range(len(package_deals))):  # Displays updated package deals
                        print("(" + str(position + 1) + ") " + package_deals[index])
                    return 1
            else:
                print("Input out of range!")
        else:
            print("Please enter an integer!")


# This function will rename a package deal from the package deal list
def rename_package(package_deals):
    while True:
        print("\nBelow is the current package deals:")
        for position, index in enumerate(range(len(package_deals))):
            print("(" + str(position + 1) + ") " + package_deals[index])
        package_selected = input("Which package deal would you like to rename or 0 to go back?: ")

        if package_selected.isdigit():
            package_index = int(package_selected)

            # If package is 0, exit
            if package_index == 0:
                return

            if package_index < len(package_deals):
                new_package_deal_name = input("\nEnter the new name for the package deal: ")

                confirmed_rename = AdditionalFunctionSportTickets.yes_or_no("\nAre you sure you want to rename the "
                                                                            "package deal, " +
                                                                            package_deals[package_index - 1]
                                                                            + ", to " + new_package_deal_name +
                                                                            "? \n(1) Yes \n(2) No\n")

                if confirmed_rename == 1:
                    package_deals[package_index - 1] = new_package_deal_name  # Renames Package Deal
                    print("Package deal has successfully been renamed...")
                    for position, index in enumerate(range(len(package_deals))):  # Displays updated package deals
                        print("(" + str(position + 1) + ") " + package_deals[index])
                    return 1
            else:
                print("Input out of range!")
        else:
            print("Please enter an integer!")


#######################################################################################################################
# This function allows admin to rename seats and then confirm if it's correct
def changing_seat_name(seat_index_valid, teams_seats):
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
            price_update = float(price_update)
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
                print("Input out of range!")
        else:
            print("Input must be a number!")
