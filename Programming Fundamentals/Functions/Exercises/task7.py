# Write a function that counts the number of
#  occurrences of a letter in a string.

def occurrences(letter, string):
    return string.count(letter)

x = occurrences('a', 'aaa') # x = 3
print(x)
x = occurrences('a', 'aabb') # x = 2
print(x)
x = occurrences('a', 'bbcc') # x = 0
print(x)
