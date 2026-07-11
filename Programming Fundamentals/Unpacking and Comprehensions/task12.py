# Task 12
# Write a comprehension that keeps only the strings which start with a vowel.

# Example

# apple, banana, cherry, date, orange
# apple, orange

strings = [string for string in input().split(", ")]
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
filtered_string = [string for string in strings if string[0] in vowels]

print(', '.join(filtered_string))
