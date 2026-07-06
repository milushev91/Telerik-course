# Task 5
# Extend and print a list with values from 
#a single line of input.

# Example:

# a, b, c, d
# input e, f, g, h
# output [a, b, c, d, e, f, g, h]

letters = ["a", "b", "c", "d"]

more_letters = input().split(", ")

for letter in more_letters:
    letters.append(letter)

print(letters)
