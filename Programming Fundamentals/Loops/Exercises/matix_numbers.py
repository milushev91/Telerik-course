n = int(input())

for row in range(1, n + 1):
    print(row, end=" ")
    
    for col in range(row + 1, n + row):
        print(col, end=" ")
    print()
