# Task 25
# Write a comprehension that stores all characters 
# as keys and all possible two-character combinations
#  starting with the key as values.

# Example:

# ["a", "b", "c", "d"]
# {'a': ['aa', 'ab', 'ac', 'ad'], 'b': ['ba', 'bb', 'bc', 'bd'], 'c': ['ca', 'cb', 'cc', 'cd'], 'd': ['da', 'db', 'dc', 'dd']}

letters = ["a", "b", "c", "d"]
letters_dic = {letter1: [letter1 + letter2 for letter2 in letters] for letter1 in letters}

print(letters_dic)
