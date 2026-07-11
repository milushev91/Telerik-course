# Task 17
# Write a comprehension that stores strings and their length.

# Example:

# ["apple", "banana", "cat", "cucumber", "elephants", "this is a longer string"]
# {'apple': 5, 'banana': 6, 'cat': 3, 'cucumber': 8, 'elephants': 9, 'this is a longer string': 23}

custom_list = ["apple", "banana", "cat", "cucumber", "elephants", "this is a longer string"]
custom_dict = {string: len(string) for string in custom_list}

print(custom_dict)
