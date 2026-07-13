# Task 26
# Write a comprehension that stores all characters as keys 
# and all possible two-character combinations starting with the 
# key as values excluding the ones built from repeating a single character.

# Example:

# ["a", "b", "c", "d"]
# {'a': ['ab', 'ac', 'ad'], 'b': ['ba', 'bc', 'bd'], 'c': ['ca', 'cb', 'cd'], 'd': ['da', 'db', 'dc']}

letters = ["a", "b", "c", "d"]
letters_dic = {letter1: [letter1 + letter2 for letter2 in letters if letter1 != letter2] for letter1 in letters}

print(letters_dic)
