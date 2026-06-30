n = int(input())

sum_numbers = 0

for num in range(1, n + 1):
    num = float(input())

    sum_numbers += num

avg = sum_numbers / n

print(f"{avg:.2f}")
