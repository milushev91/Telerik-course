# Task 5
# Write a comprehension that parses values to int from a single line of input.

# Example

# input 1 2 3 4 5
# exact output [1, 2, 3, 4, 5]

numbers = [int(num) for num in input().split()]

print(numbers)
