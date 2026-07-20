n = int(input())

matrix = [[int(num) for num in input().split()] for _ in range(n)]
matrix_cols = len(matrix[0])

print(*matrix, sep="\n")
cordinate_line = [int(num) for num in input().split()]
cordinate_line_len = len(cordinate_line)
cordinate_pairs = [cordinate_line[i:i+2] for i in range(0, cordinate_line_len, 2)]
print(cordinate_pairs)

sum_score = 0

for cordinate_pair in cordinate_pairs:
    row, col = cordinate_pair
    row_start = 0
    row_end = col
    row_step = 1

    if row < 0:
        row_start = matrix_cols - 1
        row_end -= 1
        row_step = -1 
    
    for i in range(row_start, row_end, row_step):
        sum_score += matrix[row - 1][i]
    
    for i in range(row-2, -1, -1):
        print(i)
        sum_score += matrix[row][col]
    break
print(sum_score)
