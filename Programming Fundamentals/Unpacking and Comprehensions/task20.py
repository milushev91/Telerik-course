# Task 20
# Write a comprehension that stores a string as a key and its length as a value
# if the string starts with a capital letter, otherwise swap the key and the value.

# Example:

# ["Pesho", "cat", "Gosho", "cucumber", "Tosho", "elephant"]
# {'Pesho': 5, 3: 'cat', 'Gosho': 5, 8: 'elephant', 'Tosho': 5}

strings = ["Pesho", "cat", "Gosho", "cucumber", "Tosho", "elephant"]

dictionary = {string if string[0].isupper() else len(string): string if not string[0].isupper() else len(string)  for string in strings}

print(dictionary)
