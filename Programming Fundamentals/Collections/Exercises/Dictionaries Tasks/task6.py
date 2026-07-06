# Task 6
# Print the key-value pairs from a dictionary.

# Example:

# Alice -> Marketing, Steven -> Sales, Pesho -> Management
# Alice works in Marketing
# Steven works in Sales
# Pesho works in Management

employees_info = {
    "Alice": "Marketing",
    "Steven": "Sales",
    "Pesho": "Management",
}

for employee in employees_info:
    print(f"{employee } -> {employees_info[employee]}")
