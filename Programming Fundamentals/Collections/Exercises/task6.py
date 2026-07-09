# Task 6
# Keep unique names from two different collections.

# Example:

# Pesho, Gosho, Tosho, Sasho
# Tosho, Sasho, Misho, Shisho
# output Pesho, Gosho, Misho, Shisho

first_colection = {"Pesho", "Gosho", "Tosho", "Sasho"}
second_colection = {"Tosho", "Sasho", "Misho", "Shisho"}
output = first_colection .symmetric_difference(second_colection)

print(output)
