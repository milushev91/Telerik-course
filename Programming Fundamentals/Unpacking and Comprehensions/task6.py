# Task 6
# Write a comprehension that parses values to int from 
# a single line of input and keeps only the unique ones.

# Example

# input 1 1 2 3 3 4 5 5
# exact output [1, 2, 3, 4, 5]

numbers = [int(num) for num in input().split()]

print(list(set(numbers)))
