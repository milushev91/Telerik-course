# Task 19
# Write a comprehension that repeats a string as a different element
# the amount of times specified from a dictionary.

# Example:

# {"Pesho": 3, "Gosho": 2, "Tosho": 1, "Sasho": 2}
# {3: 'Pesho', 2: 'Sasho', 1: 'Tosho'}


custom_dict = {"Pesho": 3, "Gosho": 2, "Tosho": 1, "Sasho": 2}
custom_dict_2 = {value: key for key, value in custom_dict.items()}

print(custom_dict_2)
