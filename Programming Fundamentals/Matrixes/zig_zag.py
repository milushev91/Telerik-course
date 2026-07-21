rows, cols = [int(num) for num in input().split()]

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

sum_score = matrix[0][0]

for row in range(rows - 1):

    if row % 2 == 0:
        for col in range(cols - 1):
            if col % 2 == 0:
                sum_score += matrix[row + 1][col + 1]
            else:
                
                sum_score += matrix[row][col + 1]
    else:
        for col in range(cols - 1, 0, -1):
            if col % 2 != 0:
                sum_score += matrix[row + 1][col - 1]
                
            else:
                sum_score += matrix[row][col - 1]

print(sum_score)
