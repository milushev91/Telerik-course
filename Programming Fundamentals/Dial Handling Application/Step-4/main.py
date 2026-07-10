commands_message = '''Please enter a one digit command. Valid commands are: 
"1" for the command create order
"2" for the command list (orders)
"3" for the command request help 
"0" for the command leave or exit the program'''

products = ['01.Potato', '02.Fish', '03.Apple', '04.Orange']
orders = []
help_requests = []

print(commands_message)

command = input()

while command != "0":

    if command == "1":
        print("Enter 2 digit product code or 00 to finish the order")
        print('Enter 01 for potato, 02 for fish, 03 for apple, 04 for orange and 00 if you want to finish the order')

        product_code = input()

        order = []
        while product_code != "00":
            
            if product_code == "01":
                order.append("01")
                print("Adding potato to the order")
            elif product_code == "02":
                order.append("02")
                print("Adding fish to the order")
            elif product_code == "03":
                order.append("03")
                print("Adding apple to the order")
            elif product_code == "04":
                order.append("04")
                print("Adding orange to the order")
            else:
                print("Wrong code")
            
            print("Enter 2 digit product code or 00 to finish the order")
            print('Enter 01 for potato, 02 for fish, and 00 if you want to finish the order')

            product_code = input()
        
        orders.append(" ".join(order))
        print("The order is finished")

    elif command == "2":
        print("Doing list")
        print('Here are your orders:')
        orders_count = len(orders)

        for idx in range(orders_count):
            print(f"{idx + 1}. {orders[idx]}")

    elif command == "3":
        print("Doing request")

        order_number = input("Enter order number: ")

        if not order_number.isdigit():
            print("You must pick a number i.e 1, 2, 3...")
        else:
            if 1 <= int(order_number) < len(orders):
                help_requests.append(order_number)
                print(f"Success. You have added order number {order_number} to help request")
            else:
                print("Invalid order number. Use list command to see valid orders.")

    else:
        print("Wrong command. Please enter a valid command!")
    
    print(commands_message)
    
    command = input()

print('Thank you for using our program!')
print('Summary of your interaction:')
print(f"Orders made: {', '.join(orders)}")
print(f"Help requests made: {', '.join(help_requests)}")
