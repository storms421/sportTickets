import DenverNuggetsTickets


def customer_access(teams_list, team_seats, team_prices):

    print("Check out our outstanding Colorado teams below!")
    # Loops through list of teams to present to customer
    for index in range(len(teams_list)):
        print("(" + str(index + 1) + ") " + teams_list[index])

    team_selection_number = input("\nWhich sports team are we looking to purchase tickets from?: ")  # User input

    team_selection_number = int(team_selection_number)
    if team_selection_number == 1:
        print("Broncos")
    elif team_selection_number == 2:
        DenverNuggetsTickets.denver_nuggets_tickets(team_seats, team_prices, teams_list[team_selection_number - 1])
    else:
        print("Invalid Option!")
