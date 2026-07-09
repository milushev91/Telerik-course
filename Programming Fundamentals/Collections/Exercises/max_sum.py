n = int(input())

temp_sum = int(input())
max_sum = temp_sum

for _ in range(n- 1):
    num = int(input())

    temp_sum += num 

    if temp_sum < 0:
        temp_sum = 0 
    
    if temp_sum > max_sum:
        max_sum = temp_sum

print(max_sum)
