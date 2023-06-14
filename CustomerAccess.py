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

        team_number = integer_validation(team_selection_number, teams_list)

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

        # Loop through the seating's and prices offered for selected team
        for position, index in enumerate(range(len(seats))):
            print("(" + str(position + 1) + ") " + seats[index] + " -> " + str(prices[index]))

        user_seat_selection = input("Which seat level would you like to purchase or 0 to go back?: ")

        seat_number = integer_validation(user_seat_selection, seats)

        # If valid selection, return number
        if seat_number is not None:
            return seat_number


# This function checks for integer and range of selection validation
def integer_validation(user_input, length_of_list):

    # If user puts in an integer, then convert to integer
    if user_input.isdigit():
        input_number = int(user_input)
        # If user puts in valid input, return integer
        if 1 <= input_number <= len(length_of_list):
            return input_number
        else:
            print("Invalid selection!\n")
    else:
        print("Input must be a number!\n")

