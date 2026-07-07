n = int(input())

prev_element = int(input())
max_counter = 1
num_counter = 1

for _ in range(n - 1):
    num = int(input())
    
    if prev_element == num:
        num_counter += 1 
    else:
        num_counter = 1
        
    if num_counter >= max_counter:
        max_counter = num_counter
    prev_element = num

print(max_counter)
