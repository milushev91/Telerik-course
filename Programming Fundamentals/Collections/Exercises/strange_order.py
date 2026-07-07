numbers = input().split(",")

negatives = []
positives = []
zeroes = []

for num in numbers:
    int_num = int(num)

    if int_num < 0:
        negatives.append(num)
    elif int_num > 0:
        positives.append(num)
    else:
        zeroes.append(num)

output = negatives + zeroes + positives
print(','.join(output))
