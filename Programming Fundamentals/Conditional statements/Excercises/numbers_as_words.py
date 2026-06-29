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

        if ones == 0:
            tens_output = "ten"
        elif ones == 1:
            tens_output = "eleven"
        elif ones == 2:
            tens_output = "twelve"
        elif ones == 3:
            tens_output = "thirteen"
        elif ones == 4:
            tens_output = "fourteen"
        elif ones == 5:
            tens_output = "fifteen"
        elif ones == 6:
            tens_output = "sixteen"
        elif ones == 7:
            tens_output = "seventeen"
        elif ones == 8:
            tens_output = "eighteen"
        elif ones == 9:
            tens_output = "nineteen"
    
    if tens > 1:
        if tens == 2:
            tens_output = "twenty "
        elif tens == 3:
            tens_output = "thirty "
        elif tens == 4:
            tens_output = "fourty "
        elif tens == 5:
            tens_output = "fifty "
        elif tens == 6:
            tens_output = "sixty "
        elif tens == 7:
            tens_output = "seventy "
        elif tens == 8:
            tens_output = "eighty "
        elif tens == 9:
            tens_output = "ninety "

    if hundreds >= 1:
        if hundreds == 1:
            hundreds_output = "one hundred"        
        elif hundreds == 2:
            hundreds_output = "two hundred"        
        elif hundreds == 3:
            hundreds_output = "three hundred"        
        elif hundreds == 4:
            hundreds_output = "four hundred"        
        elif hundreds == 5:
            hundreds_output = "five hundred"        
        elif hundreds == 6:
            hundreds_output = "six hundred"        
        elif hundreds == 7:
            hundreds_output = "seven hundred"        
        elif hundreds == 8:
            hundreds_output = "eight hundred"        
        elif hundreds == 9:
            hundreds_output = "nine hundred"
        
        
        if tens > 0 or ones > 0:
                
            hundreds_output += " and "

    print(f"{hundreds_output}{tens_output}{ones_output}")
