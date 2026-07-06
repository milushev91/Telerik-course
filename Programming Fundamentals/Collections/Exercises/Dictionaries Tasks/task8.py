# Task 8
# Create a new dictionary from an existing one with swapped key-value pairs.

# Example:

# dct = Alice -> Marketing, Steven -> Sales, Pesho -> Management
# output Marketing -> Alice, Sales -> Steven, Management -> Pesho


employees_info = {
    "Alice": "Marketing",
    "Steven": "Sales",
    "Pesho": "Management",
}

new_employees_info = {}

for key, value in employees_info.items():
    new_employees_info[value] = key

print(new_employees_info)
