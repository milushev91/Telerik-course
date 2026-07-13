# Write a comprehension that stores all three-character combinations in a list.

# Example:

# ["a", "b", "c"]
# ['aaa', 'aab', 'aac', 'aba', 'abb', 'abc', 'aca', 'acb', 'acc', 'baa', 'bab', 'bac', 'bba', 'bbb', 'bbc', 'bca', 'bcb', 'bcc', 'caa', 'cab', 'cac', 'cba', 'cbb', 'cbc', 'cca', 'ccb', 'ccc']


letters = ["a", "b", "c", "d"]
letter_combinations = [letter1 + letter2 + letter3 for letter3 in letters for letter1 in letters for letter2 in letters]
print(letter_combinations)
