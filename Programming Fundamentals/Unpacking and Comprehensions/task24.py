# Task 24
# Write a comprehension that stores all four-character combinations in a list.

# Example:

# ["a", "b"]
# ['aaaa', 'aaab', 'aaba', 'aabb', 'abaa', 'abab', 'abba', 'abbb', 'baaa', 'baab', 'baba', 'babb', 'bbaa', 'bbab', 'bbba', 'bbbb']

letters = ["a", "b", "c", "d"]
letter_combinations = [letter1 + letter2 + letter3 + letter4 for letter4 in letters for letter3 in letters for letter1 in letters for letter2 in letters]
print(letter_combinations)
