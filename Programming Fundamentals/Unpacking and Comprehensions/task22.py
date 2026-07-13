# Write a comprehension that stores all two-character combinations in a list.

# Example:

# ["a", "b", "c", "d"]
# ['aa', 'ab', 'ac', 'ad', 'ba', 'bb', 'bc', 'bd', 'ca', 'cb', 'cc', 'cd', 'da', 'db', 'dc', 'dd']

letters = ["a", "b", "c", "d"]
letter_combinations = [letter1 + letter2 for letter1 in letters for letter2 in letters]
print(letter_combinations)
