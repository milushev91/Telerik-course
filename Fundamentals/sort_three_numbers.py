num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 > num2 and num1 > num3:
    print(num1, end=" ")
    
    if num2 >= num3:
        print(f"{num2} {num3}")
    else:
        print(f"{num3} {num2}")
        
elif num2 > num1 and num2 > num3:
    print(num2, end=" ")
    
    if num1 >= num3:
        print(f"{num1} {num3}")
    else:
        print(f"{num3} {num1}")
        
elif num3 > num1 and num3 > num2:
    print(num3, end=" ")
    
    if num1 >= num2:
        print(f"{num1} {num2}")
    else:
        print(f"{num2} {num1}")
else:
    print(f"{num1} {num2} {num3}")
