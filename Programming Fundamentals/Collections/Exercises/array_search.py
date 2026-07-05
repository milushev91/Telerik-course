numbers = input().split(",")

n = len(numbers)
unique_numbers = []

for num in range(1, n + 1):
    str_num = str(num)
    
    if str_num not in numbers:
        unique_numbers.append(str_num)

print(",".join(unique_numbers))
