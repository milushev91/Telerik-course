n = int(input())

for row in range(n):
    for col in range(row + 1, row + 1 + n):
        print(col, end=" ")
    print()
