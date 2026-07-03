print('''Please enter a one digit command. Valid commands are: 
"1" for the command create order
"2" for the command list (orders)
"3" for the command request help 
"0" for the command leave or exit the program''')

command = input()

while command != "0":

    if command == "1":
        print("Enter 2 digit product code or 00 to finish the order")
        print('Enter 01 for potato, 02 for fish, and 00 if you want to finish the order')

        product_code = input()

        while product_code != "00":
            if product_code == "01":
                print("Adding potato to the order")
            elif product_code == "02":
                print("Adding fish to the order")
            else:
                print("Wrong code")
            
            print("Enter 2 digit product code or 00 to finish the order")
            print('Enter 01 for potato, 02 for fish, and 00 if you want to finish the order')

            product_code = input()
            
        print("The order is finished")

    elif command == "2":
        print("Doing list")
    elif command == "3":
        print("Doing request")
    else:
        print("Wrong command. Please enter a valid command!")
    
    print('''Please enter a one digit command. Valid commands are: 
        "1" for the command create order
        "2" for the command list (orders)
        "3" for the command request help 
        "0" for the command leave or exit the program''')
    
    command = input()

print("Thank you")
