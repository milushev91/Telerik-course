# product variables
first_product_name = "01.Potato"
second_product_name = "02.Fish"
third_product_name = "03.Apple"

# message variables
create_order_message = "Menu: Dial only one digit:1 - Create order"
add_product_message = "Enter the 2 digit product code to add it to the order"
thank_you_message = "Thank you for using our program!"
summary_message = "Summary of your interaction: "

# get command number for user
user_choice = int(input("Pick command operation number: "))

# print available products
print(f"Here are our products: {first_product_name}, {second_product_name}, {third_product_name}")

# print prompt message to user to pick products
print(add_product_message)

# ask user for product code and print confirmation message 3 times
first_product_code = input("Enter first product code: ")
print(f"Product with code: {first_product_code} was added to the order")

second_product_code = input("Enter second product code: ")
print(f"Product with code: {second_product_code} was added to the order")

third_product_code = input("Enter third product code: ")
print(f"Product with code: {third_product_code} was added to the order")

# print thank you and summary message
print(thank_you_message)
print(summary_message)

# print order summary
print(f"Orders: 1 order containing [{first_product_code}, {second_product_code}, {third_product_code}]")
