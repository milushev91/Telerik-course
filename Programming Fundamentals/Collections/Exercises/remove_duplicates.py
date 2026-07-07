numbers = input().split(",")

unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print(','.join(unique_numbers))
