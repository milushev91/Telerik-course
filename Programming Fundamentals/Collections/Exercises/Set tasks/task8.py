# Task 8
# Print if each value from a set 
# (single line console input) is in another set.

# Example:

# a, b, c, d
# input a, e, b, f, c, g, d, h
# output on separate lines True False
# True False True False True False

first_set = {"a", "b", "c", "d"}
second_set = set(input().split(", "))

for item in second_set:
    
    print(item in first_set, end=" ")
