numbers = input().split(",")

non_zeroes = []
zeroes = []

for num in numbers:

    if num == "0":
        zeroes.append(num)
        continue
    non_zeroes.append(num)

output = non_zeroes + zeroes
print(",".join(output))
