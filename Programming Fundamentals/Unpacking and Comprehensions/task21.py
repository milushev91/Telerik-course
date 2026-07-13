# Task task21
# Write a comprehension that stores only even length strings 
# as keys and their length as values if the string starts with a capital letter, otherwise swap the key and the value.

# Example:

# ["Pesho", "cat", "Gosho", "cucumber", "Tosho", "elephant", "Shisho"]
# {8: 'elephant', 'Shisho': 6}

strings = ["Pesho", "cat", "Gosho", "cucumber", "Tosho", "elephant", "Shisho"]
dictionary = {string if string[0].isupper() else len(string) : string if not string[0].isupper() else len(string) for string in strings if len(string) % 2 == 0}
print(dictionary)
