numbers = [int(num) for num in input().split(",")]

sum_numbers = sum(numbers)
len_numbers = len(numbers)
avg = sum_numbers / len_numbers

bellow_avg = []
above_avg = []

for num in numbers:
    if num < avg:
        bellow_avg.append(str(num))
    elif num > avg:
        above_avg.append(str(num))

print(f"avg: {avg:.2f}")
print(f"below: {','.join(bellow_avg)}")
print(f"above: {','.join(above_avg)}")
