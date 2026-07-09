n = int(input())

for _ in range(n):
    numbers = input().split()

    i = 0
    j = len(numbers) - 1 

    while True:
        
        if i >= j:
            print("Yes")
            break 
            
        if numbers[i] != numbers[j]:
            print("No")
            break
        i += 1
        j -= 1
