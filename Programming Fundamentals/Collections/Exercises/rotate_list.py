numbers = input().split(",")
n = int(input())

for _ in range(n):
    numbers.append(numbers.pop(0))

print(*numbers, sep=",")
