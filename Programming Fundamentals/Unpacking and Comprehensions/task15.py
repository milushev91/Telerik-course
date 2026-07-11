# Task 15
# Write a comprehension that reverses and converts strings to uppercase.

# Example

# ["hello", "world", "python", "list"]
# ['OLLEH', 'DLROW', 'NOHTYP', 'TSIL']


start_list = ["hello", "world", "python", "list"]
end_list = [string.upper()[::-1] for string in start_list]

print(end_list)
