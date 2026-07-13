numbers = [num for num in input().split()]

num_groups = {0: [], 1: [], 2: []}

for num in numbers:
    remainder = int(num) % 3

    num_groups[remainder].append(num)

for line in num_groups.values():
    print(" ".join(line))
