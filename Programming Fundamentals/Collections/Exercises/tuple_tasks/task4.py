# Task 4
# Print if a value (console input) is in a tuple.

# Example:

# 1, 2, 3, 4
# value = 2 -> output True
# value = 5 -> output False


new_tuple = tuple(input().split(", "))
value = input()

print(value in new_tuple)
