import DenverNuggetsTickets


# This function is used to select teams for purchasing tickets
def select_team(teams_list):
    # While user is selecting, loop through teams
    while True:
        # Lists all Colorado teams in array
        print("Check out our outstanding Colorado teams below!")
        # Loops through list of teams to present to customer
        for index in range(len(teams_list)):
            print("(" + str(index + 1) + ") " + teams_list[index])

        # Looks for customers selection and returns when matched
        team_selection_number = input(
            "\nWhich sports team are we looking to purchase tickets from? (Enter the number): ")
        if team_selection_number.isdigit() and 1 <= int(team_selection_number) <= len(teams_list):
            return teams_list[int(team_selection_number) - 1]  # Makes sure to return team in correct index
        else:
            print("Invalid input. Please try again.\n")
