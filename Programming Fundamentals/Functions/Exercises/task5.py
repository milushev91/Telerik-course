# 1. Write a function that sums only the digits in a string

def sum_digits(string):
    digit_sum = 0 

    for char in string:
        if char.isdigit():
            digit_sum += int(char)
    
    return digit_sum


x = sum_digits('abc123a4') # x = 10
print(x)
x = sum_digits('abc') # x = 0
