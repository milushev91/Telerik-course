# Task 8
# Print if each value from a list 
# (single line console input) is in 
# another list.

# Example:

# a, b, c, d
# input a, e, b, f, c, g, d, h
# output on separate lines True False True False True False True False

letters = ["a", "b", "c", "d"]
other_letters = input().split(", ")

for letter in other_letters:
    print(letter in letters)




