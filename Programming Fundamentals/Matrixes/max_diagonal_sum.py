n = int(input())

matrix = [[int(num) for num in input().split()] for _ in range(n)]

total = 0

for i in range(n):
    total += matrix[i][i]  # primary diagonal

for i in range(n):
    if i != n - 1 - i:  # skip cells already in primary diagonal
        total += matrix[i][n - 1 - i]

print(total)
