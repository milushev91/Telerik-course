# Task 14
# Write a comprehension that counts the amount of times a name appears 
# in a list and stores both.

# Example

# ["Pesho", "Pesho", "Gosho", "Gosho", "Tosho", "Pesho", "Sasho", "Gosho", "Sasho",
# "Pesho"]
# {"Pesho": 4, "Gosho": 3, "Tosho": 1, "Sasho": 2}

custom_list = ["Pesho", "Pesho", "Gosho", "Gosho", "Tosho", "Pesho", "Sasho", "Gosho", "Sasho",
"Pesho"]

custom_dictionary = {name: custom_list.count(name) for name in custom_list}

print(custom_dictionary)
