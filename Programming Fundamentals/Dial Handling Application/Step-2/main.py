print('''Please enter a 3 digit code. All characters must be digits''')

# prompt the user for a 3 digit code
three_digits_input = input()

# check for invalid input length
if len(three_digits_input) != 3:
    #display error message
    print("Invalid number of characters in the input: must be 3")
else:
    # valid input == 3 digit characters
    if (three_digits_input.isdigit()):
        # print confirmation message
        print("Input accepted")
    else:
        # print error message for containing non-digit characters
        print("Input must contain digits only!")
