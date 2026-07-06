# Task 4
# Print the indices of elements 
# in a tuple from another tuple 
# (single line console input).

# Example:

# a, b, c, d
# input d c b a
# output on separate lines 3 2 1 0
# input c a b d
# output on separate lines 2 0 1 3


my_tuple = ("a", "b", "c", "d")

another_tuple = tuple(input().split())

for item in another_tuple:
    print(my_tuple.index(item), end=" ")
