# Task 4
# Print if a value (console input)
#is in a dictionary.

# Example:

# name -> Alice, age -> 29, city -> London
# input Alice -> output True
# input Steven -> output False

persons_info = {
    "name": "Alice",
    "age": 29,
    "city": "London",
}

value = input()

print(value in persons_info.values())
