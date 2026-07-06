# Task 7
# Update a set with multiple 
# values from a single line 
# console input and print the set.

# Example:

# a, b, c, d
# input e f g h a d
# output a, b, c, d, e, f, g, h

first_set = {"a", "b", "c", "d"}
second_set = set(input().split())
combined_set = first_set.union(second_set)

print(combined_set)
