matrix = [[int(num) for num in line.split()] for line in input().split(",")]

rows = len(matrix)
cols = len(matrix[0])

diagonals = []

# Start from left column, bottom → top
for start_row in range(rows - 1, -1, -1):
    r = start_row
    c = 0
    diag = []
    while r < rows and c < cols:
        diag.append(matrix[r][c])
        r += 1
        c += 1
    diagonals.append(diag)

# 2Continue from top row, columns 1 → end
for start_col in range(1, cols):
    r = 0
    c = start_col
    diag = []
    while r < rows and c < cols:
        diag.append(matrix[r][c])
        r += 1
        c += 1
    diagonals.append(diag)

for diagonal in diagonals:
    if diagonal.count(diagonal[0]) != len(diagonal):
        print("false")
        break 
else:
    print("true")
