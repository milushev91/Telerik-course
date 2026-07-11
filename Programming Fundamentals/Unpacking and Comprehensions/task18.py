# Task 18
# Write a comprehension that repeats a string as a different element
# the amount of times specified from a dictionary.

# Example:

# {"Pesho": 3, "Gosho": 2, "Tosho": 1, "Sasho": 2}
# ['Pesho', 'Pesho', 'Pesho', 'Gosho', 'Gosho', 'Tosho', 'Sasho', 'Sasho']


custom_dict = {"Pesho": 3, "Gosho": 2, "Tosho": 1, "Sasho": 2}
custom_list = [key for key, value in custom_dict.items() for _ in range(value)]

print(custom_list)
