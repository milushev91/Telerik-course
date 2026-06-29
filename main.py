num = int(input())
 
if num == 0:
    print("zero")
else:
    hundreds = num // 100
    tens = ((num - hundreds * 100) // 10)
    ones = num - hundreds * 100 - tens * 10
    
    ones_output = ""
    tens_output = ""
    hundreds_output = ""
    
    if ones > 0 and tens != 1:
        if ones == 1:
            ones_output = "one"
        elif ones == 2:
            ones_output = "two"
        elif ones == 3:
            ones_output = "three"
        elif ones == 4:
            ones_output = "four"
        elif ones == 5:
            ones_output = "five"
        elif ones == 6:
            ones_output = "six"
        elif ones == 7:
            ones_output = "seven"
        elif ones == 8:
            ones_output = "eight"
        elif ones == 9:
            ones_output = "nine"
 
    if tens == 1 and ones >= 0:
        ones_output = ""
        
        if num == 10:
            tens_output = "ten"
        elif num == 11:
            tens_output = "eleven"
        elif num == 12:
            tens_output = "twelve"
        elif num == 13:
            tens_output = "thirteen"
        elif num == 14:
            tens_output = "fourteen"
        elif num == 15:
            tens_output = "fifteen"
        elif num == 16:
            tens_output = "sixteen"
        elif num == 17:
            tens_output = "seventeen"
        elif num == 18:
            tens_output = "eighteen"
        elif num == 19:
            tens_output = "nineteen"
    if tens >= 1:
        if te
