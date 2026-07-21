rows = int(input())
cols = int(input())
moves = int(input())
codes = [int(code) for code in input().split(" ")]
 
matrix = [[0]*cols for _ in range(rows)]
power = 0
 
for i in range(rows - 1, -1, -1):
    for j in range(cols):
        matrix[i][j] = 2**(j + power)
    power += 1
 
result = 1
curr_row = rows - 1
curr_col = 0
coeff = max(rows, cols)
 
for i in range(len(codes)):
    next_row = codes[i] // coeff
    next_col = codes[i] % coeff
    start_row = min(curr_row, next_row)
    end_row = max(curr_row, next_row)
    start_col = min(curr_col, next_col)
    end_col = max(curr_col, next_col)
 
    for j in range(start_col, end_col + 1):
        if j != curr_col:
            result += matrix[curr_row][j]
        matrix[curr_row][j] = 0
 
    curr_col = next_col
 
    for j in range(start_row, end_row + 1):
        if j != curr_row:
            result += matrix[j][curr_col]
        matrix[j][curr_col] = 0
 
    curr_row = next_row
 
print(result)
