# Overview



Create an app that answers calls from customers. In the beginning, a list of products must be listed in the console. Then there must be a system that handles the user input to perform the following operations: 1 Make an order 2 List all user orders 3 Request help with an order (the request will be handled by another system, only a log of the order number should be saved) 4 Request to cancel an order (save the order number - another system will handle the order deletion after company representative approval) Use variables, conditional statements, loops, and lists in combination to create the console application! Read and output the data on the console. Parse the input where needed. Think about how to handle invalid input (letters or characters that are not digits).



## Main menu



While in the main menu, the user should enter only one digit to select a valid command for the program. The valid commands are:

* 1 for making an order
* 2 for listing all the orders of the user
* 3 to request help with an order
* 4 to request cancellation of an order
* 0 to exit the main menu and the program



## Products



For this program products will be represented by code and name combined in a single string. Here is a list of example products:

* "01.Potato", "02.Fish", "03.Apple"
* "04.Orange", "05.Milk", "06.Music"



## Implement Make Order command



First the user must get two messages:

* "Enter 2 digit product code or 00 to finish the order"
* "Here are the products and their codes: {products}" - where {products} is the list of the available products (with their codes) In this command the user must enter two digit codes of the products wanted to be added in the order. Order is a string that contains two-digit product codes separated by one space.
* for example \["01 03", "02"] are two orders. The first is for Potato and Apple and the second is just for Fish
* User should add "00" instead of the product code to finish the order

  * At this point, the order must be saved in a list of orders



## Implement the List Orders command



* Print "You have no orders" if there are no orders
* Print "Here are your orders:" followed by all orders. Each order must be displayed with a number! (see below)



Implement Request Help command

---

* Print message: "Please enter the number of your order which you need help with and one of our representatives will contact you: "
* Valid order number is required - valid number depends on the implementation of the List Orders command. For example, if the List command prints "Here are your orders:"

  * Order #: 1 Order: "01 03"
  * Order #: 2 Order: "02" Then the valid order numbers are 1 and 2.
* Add it to the list of help requests



## Implement the Request Order Cancellation command



* Print message: "Please enter the number of your order which you want to cancel and one of our representatives will review and remove it for you: "
* Valid order number is required - (see the previous command)
* Add it to the list of cancellation requests



## Implement the **Exit the Program** command



* Print "Thank you for using our program!", "Summary of your interaction: " and then the orders, help requests, and cancellation requests made by the user.
* You may format the orders, help requests, and cancellation requests as you like but keep it readable.

