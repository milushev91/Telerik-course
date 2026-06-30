n = int(input())

max_number = float("-inf")

for num in range(1, n + 1):
    num = int(input())

    if num > max_number:
        max_number = num 

print(max_number)
