n = int(input())

min_num = float("inf")
max_num = float("-inf")
sum_numbers = 0

for num in range(n):
    num = float(input())

    sum_numbers += num

    if num < min_num:
        min_num = num 
    
    if num > max_num:
        max_num = num

avg = sum_numbers / n

print(f"min={min_num:.2f}")
print(f"max={max_num:.2f}")
print(f"sum={sum_numbers:.2f}")
print(f"avg={avg:.2f}")
