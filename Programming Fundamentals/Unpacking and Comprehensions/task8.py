# Task 8
# Write a comprehension that stores ints and 
# their squares from a single line of console input.

# Example

# input 1 2 3 4 5
# exact output {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


numbers = {int(num): int(num) ** 2 for num in input().split()}

print(numbers)











