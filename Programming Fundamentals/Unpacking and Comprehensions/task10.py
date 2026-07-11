# Task 10
# Write a comprehension that keeps only 
# the strings which are longer than 5 symbols.

# Example:

# cat, dog, elephant, cucumber
# elephant, cucumber

strings = [string for string in input().split(", ") if len(string) > 5]

print(', '.join(strings))
