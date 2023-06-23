import AdditionalFunctionSportTickets


# This function is used to select teams for purchasing tickets
def select_team(teams_list):
    # While user is selecting, loop through teams
    while True:
        # Lists all Colorado teams in array
        print("Check out our outstanding Colorado teams below!")
        # Loops through list of teams to present to customer (Use enumerate for listing index)
        for index, team_names in enumerate(teams_list.keys()):
            print("(" + str(index + 1) + ") " + team_names)

        # Looks for customers selection and returns when matched
        team_selection_number = input(
            "\nWhich sports team are we looking to purchase tickets from? (Enter the number): ")

        team_number = AdditionalFunctionSportTickets.integer_validation(team_selection_number, teams_list)

        # If valid selection, return number
        if team_number is not None:
            return team_number


# This function is used to display all the team information and prompt for seat selection
def seat_selection(team_index, teams_data_info):
    while True:
        selected_team = list(teams_data_info.keys())[team_index - 1]  # Converts dictionary keys into a list, stores it
        team_details = teams_data_info[selected_team]  # Retrieves appropriate seats and prices and stores it
        print("\nWelcome to the " + selected_team + " ticket service!")

        # Pull the respected seats and prices and stores them
        seats = team_details["Seats"]
        prices = team_details["Prices"]

        # If there is a sale going on, let customer know
        if "Percentage" in team_details:
            sales_percentage = team_details["Percentage"]
            print("\nAll tickets today are {:.0f}".format((sales_percentage * 100)) + "% off today!\n")
        # If there is a charity going on, let customers know
        if "Charity" in team_details:
            charity_percentage = team_details["Charity"]
            print("\nWe will be giving {:.0f}".format((charity_percentage * 100)) +
                  "% of your purchase to charity today!\n")

        # Loop through the seating's and prices offered for selected team
        for position, index in enumerate(range(len(seats))):
            print("(" + str(position + 1) + ") " + seats[index] + " -> {:.2f}".format(prices[index]))

        user_seat_selection = input("\nWhich seat level would you like to purchase? (Enter the number): ")

        seat_number = AdditionalFunctionSportTickets.integer_validation(user_seat_selection, seats)

        # If valid selection, return number
        if seat_number is not None:
            return seat_number


# This function grabs the package deal selected by user and returns to main
def ticket_quantity(seat_price, package_deals):
    while True:
        print("\nBelow is our package deals!")
        for position, index in enumerate(range(len(package_deals))):
            print("(" + str(position + 1) + ") " + package_deals[index])

        user_package_selected = input("Which package deal would you like to purchase? (Enter the number): ")

        package_number = AdditionalFunctionSportTickets.integer_validation(user_package_selected, package_deals)

        if package_number is not None:
            return package_number
