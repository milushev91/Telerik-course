# Write a function that returns the letter which occurs
#  more often than another letter in a text. 
# Use the function from the previous exercise.

def occurrences(letter, string):
    return string.count(letter)

def stronger_letter(string, letter1, letter2):
    letter1_occurrences = occurrences(letter1, string)
    letter2_occurrences = occurrences(letter2, string)

    if letter1_occurrences >= letter2_occurrences:
        return letter1
    else:
        return letter2

x = stronger_letter('abca', 'a', 'b') # x = 'a'
print(x)
x = stronger_letter('abbca', 'c', 'b') # x = 'b'
print(x)
x = stronger_letter('aabbc', 'b', 'a') # x = 'b' (return the first one in case of a tie)
print(x)


