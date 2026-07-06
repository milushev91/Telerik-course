# Task 7
# Compare if a dictionary is identical 
# to another dictionary.

# Example:

# dct1 = Alice -> Marketing, Steven -> Sales, Pesho -> Management
# dct2 = Alice -> Marketing, Steven -> Sales, Pesho -> Management
# output True
# dct1 = Alice -> Marketing, Steven -> Sales, Pesho -> Management
# dct2 = Alice -> HR, Steven -> Sales, Pesho -> Management
# output False
# dct1 = Alice -> Marketing, Steven -> Sales, Pesho -> Management
# dct2 = Gosho -> Marketing, Steven -> Sales, Pesho -> Management
# output False

employees_info_1 = {
    "Alice": "Marketing",
    "Steven": "Sales",
    "Pesho": "Management",
}

employees_info_2 = {
    "Alice": "Marketing",
    "Steven": "Sales",
    "Pesho": "Managemesnt",
}

print(employees_info_1 == employees_info_2)

