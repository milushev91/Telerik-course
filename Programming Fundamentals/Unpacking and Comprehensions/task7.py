# Task 7
# Write a comprehension that parses
# only the digits to int from a console input string.

# Example

# input th1s i5 @ 7e5t 5str1n9 f0r a c0mpr3hen510n
# exact output [1, 5, 7, 5, 5, 1, 9, 0, 0, 3, 5, 1, 0]

numbers = [int(char) for char in input() if char.isdigit()]

print(numbers)
