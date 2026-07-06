# Task 7
# Compare if a tuple 
#(single line console input) is 
#identical to another tuple.

# Example:

# a, b, c, d
# input a b c d
# output True
# input a b c e
# output False

my_tuple = ("a", "b", "c", "d")

another_tuple = tuple(input().split())

print(my_tuple == another_tuple)
