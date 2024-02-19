# This function checks for integer and range of selection validation
def integer_validation(prompt, max_input, min_input, cast_switch):

    while True:

        selection = input(prompt)

        # If user puts in an integer, then convert to integer
        if selection.isdigit():
            if cast_switch == 0:
                input_number = int(selection)
            elif cast_switch == 1:
                input_number = float(selection)

            # If user puts in valid input, return integer
            if min_input <= input_number <= max_input or input_number == 0:
                return input_number
            else:
                print("Invalid selection!")
        else:
            print("Input must be an integer!")


# This function is used for all yes and no prompts and returns the selection
def yes_or_no(prompt):
    while True:
        is_yes = input(prompt)

        if is_yes.isdigit():
            is_yes = int(is_yes)
            if is_yes == 1 or is_yes == 2:  # 1 is always Yes and 2 is always No
                return is_yes
            else:
                print("Invalid Input")
        else:
            print("Please input an integer!")



# Take the integer validation function and pull in user inputs like the yes_or_no and have it loop until it gets the
# correct input. Can have "0" return a switch to go back when it returns. The inputs going into the function should be
# max, min, and prompt. The rest will stay the same for every case needed.
