# 2. Write a function that 'merges' two equal length numbers. 
# The merging operation adds the digits that 
# are in the same positions and if the result is greater than 9, only the 
# last digit remains. So 1 + 2 = 3, but 8 + 5 = 3 also.

def merge(num1, num2):
    num1_str, num2_str = str(num1), str(num2)
    num1_str_len = len(num1_str)
    result = ""

    for idx in range(num1_str_len):
        num1_digit = int(num1_str[idx])
        num2_digit = int(num2_str[idx])

        sum_digits = num1_digit + num2_digit

        if sum_digits > 9:
            sum_digits = str(sum_digits)[-1]
        
        result += str(sum_digits)
    
    return result
    
x = merge(123, 123) # x = 246
x = merge(789, 123) # x = 802 (7 + 1 = 8, 8 + 2 = 10, 9 + 3 = 12)
print(x)

