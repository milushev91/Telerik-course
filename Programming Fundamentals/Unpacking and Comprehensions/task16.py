# Task 16
# Write a comprehension that stores each digit from an int and
# if it is even or odd.

# Example

# 12345 (int not str)
# {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}

number = 12345

custom_dictionary = {int(digit): "odd" if int(digit) % 2 != 0 else "even" for digit in str(number)}

print(custom_dictionary)
