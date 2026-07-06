# Task 3
# Print the n-th (console input) element of a tuple.

# Example:

# 1, 2, 3, 4
# n = 2 -> output 3

new_tuple = tuple(input().split(", "))
n = int(input())

print(new_tuple[n])
