# Task 4
# Print if a value (console input) is in a set.

# Example:

# 1, 2, 3, 4
# value = 2 -> output True
# value = 5 -> output False


items = input().split(", ")
value = input()

new_set = set(items)

print(value in new_set)
    



