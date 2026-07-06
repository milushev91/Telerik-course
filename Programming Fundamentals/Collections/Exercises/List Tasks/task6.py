# Task 6
# Insert an element in a list 
#on a given index and print the list. 
#Both the element and the index are 
#console inputs.

# Example:

# a, b, c, d
# input 1 e
# output [a, e, b, c, d]

letters = ["a", "b", "c", "d"]
index = int(input())
letter = input()

letters.insert(1, letter)

print(letters)
