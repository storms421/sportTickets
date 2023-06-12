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

        # If user put in an integer, then convert to integer
        if team_selection_number.isdigit():
            team_number = int(team_selection_number)
            # If user put in a valid input, return selection integer
            if 1 <= team_number <= len(teams_list):
                return team_number
            else:
                print("Invalid selection!\n")
        else:
            print("Input must be a number!\n")


# This function is used to display all the team information and prompt for seat selection
def team_information(team_index, teams_data_info):
    selected_team = list(teams_data_info.keys())[team_index - 1]  # Converts dictionary keys into a list and stores it
    team_details = teams_data_info[selected_team]  # Retrieves appropriate seats and prices and stores it
    print("\nWelcome to the " + selected_team + " ticket service!")

    # Pull the respected seats and prices and stores them
    seats = team_details["Seats"]
    prices = team_details["Prices"]

    # Loop through the seatings and prices offered for selected team
    for position, index in enumerate(range(len(seats))):
        print("(" + str(position + 1) + ") " + seats[index] + " -> " + str(prices[index]))

