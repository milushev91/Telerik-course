n = int(input())

for _ in range(n):
    numbers = [int(num) for num in input().split(",")]
    
    prev_number = numbers[0]
    numbers_len = len(numbers)
    
    for i in range(1, numbers_len):
        current_number = numbers[i]
        
        if prev_number > current_number:
            print("false")
            break 
        
        prev_number = current_number
    else:
        print("true")
