# This function checks for integer and range of selection validation
def integer_validation(user_input, length_of_list):

    # If user puts in an integer, then convert to integer
    if user_input.isdigit():
        input_number = int(user_input)
        # If user puts in valid input, return integer
        if 1 <= input_number <= len(length_of_list):
            return input_number
        else:
            print("Invalid selection!")
    else:
        print("Input must be a number!")


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
