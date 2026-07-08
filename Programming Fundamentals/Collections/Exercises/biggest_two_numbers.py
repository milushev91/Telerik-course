numbers = [int(num) for num in input().split()]

#8 7 8 11 7 11 5 8 10

sorted_numbers = sorted(numbers, reverse=True)

print(*sorted_numbers[:2], sep=" ")
