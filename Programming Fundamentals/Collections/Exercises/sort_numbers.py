numbers = [int(num) for num in input().split(", ")]

#2, 3, 1, 5, 6

sorted_numbers = sorted(numbers, reverse=True)

print(*sorted_numbers, sep=", ")
