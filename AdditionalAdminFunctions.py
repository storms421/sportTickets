import AdditionalFunctionSportTickets


# This function will add seats to the sports team dictionary for customer
def add_seats(selected_team_name, seats, prices):
    while True:
        new_seat = input("\nEnter the new seat name or 0 to go back: ")

        # If user enters 0, go back to submenu
        if new_seat == "0":
            break

        new_price = input("Enter the price for the new seat: ")

        confirmed_add = AdditionalFunctionSportTickets.yes_or_no("\nBelow is the new seat and price:\n\t" + new_seat +
                                                              " -> " + new_price + "\nIs this correct?: "
                                                              "\n(1) Yes \n(2) No\n")
        # If confirmed name and prices, add to end of dictionary list
        if confirmed_add == 1:
            seats.append(new_seat)
            prices.append(new_seat)
            return 1  # Returns to ask admin if they would like to modify more


# This function will remove seats from the sports team dictionary for the customers
def delete_seats(selected_team_name, seats, prices):
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
                del seats[seat_index - 1]
                del prices[seat_index - 1]

                print("\nSeat and price has successfully been deleted...")
                # Lists selected sports teams seating
                for index, seat_names in enumerate(seats):
                    print("(" + str(index + 1) + ") " + seat_names)
                return 1  # Returns to ask admin if they would like to modify more


# This function will rename the seats for the sports team dictionary for the customer
def rename_seats(selected_team_name, seats, prices):
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
