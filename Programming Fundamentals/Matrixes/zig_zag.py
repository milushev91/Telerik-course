rows, cols = [int(num) for num in input().split()]
print(rows, cols)

matrix = []
row_start = 1 
for i in range(rows):
    col_start = row_start
    row = []

    for j in range(cols):
        row.append(col_start)
        col_start += 3 

    matrix.append(row)
    row_start += 3

for row in range(rows):

    if row % 2 == 0:
        for col in range(cols - 1):
            if col % 2 == 0:
                print(matrix[row + 1][col + 1])
            else:
                print(matrix[row][col + 1])
    else:
        for col in range(cols - 1, 0, -1):
            if col % 2 != 0:
                print(mat)

    break
print(*matrix, sep="\n")

