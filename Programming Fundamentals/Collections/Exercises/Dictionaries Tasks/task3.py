# Task 3
# Print if a key (console input) is in a dictionary.

# Example:

# name -> Alice, age -> 29, city -> London
# input name -> output True
# input address -> output False

persons_info = {
    "name": "Alice",
    "age": 29,
    "city": "London",
}

key = input()

print(key in persons_info)
