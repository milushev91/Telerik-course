# Task 1
# Count the frequency of each character in a string (console input).

# Example:

# input hello
# output h -> 1, e -> 1, l -> 2, o -> 1

string = input()
chars_count = {}

for char in string:

    if char not in chars_count:
        chars_count[char] = 0

    chars_count[char] += 1

for key, value in chars_count.items():
    print(f"{key} -> {value}", end=", ")
