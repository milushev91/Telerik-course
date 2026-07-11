# Task 9
# Write a comprehension that parses to int and stores only the
# values (single line console input) that are less than 5 or 
#larger than 15.

# Example:

# input 1 15 6 25 9 35 4 5 6 45 78
# exact output [1, 25, 35, 4, 45, 78]

numbers = [int(num) for num in input().split() if int(num) < 5 or int(num) > 15]

print(numbers)
