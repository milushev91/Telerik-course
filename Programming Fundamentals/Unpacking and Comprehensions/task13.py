# Task 13
# Write a comprehension that repeats a symbol the amount of
# times specified from a dictionary.

# Example:

# {"a": 1, "b": 2, "c": 3, "d": 1}
# ["a", "bb", "ccc", "d"]

dictionary = {"a": 1, "b": 2, "c": 3, "d": 1}

custom_list = [key * value for key, value in dictionary.items()]

print(custom_list)
