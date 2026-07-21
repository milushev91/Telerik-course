n = int(input())
 
matrix = [n*[0] for _ in range(n)]
 
knight_moves = [
    [-2, -1],
    [-2, 1],
    [-1, -2],
    [-1, 2],
    [1, -2],
    [1, 2],
    [2, -1],
    [2, 1]
]
 
move = 1
 
for row in range(n):
    for col in range(n):
        current_row = row
        current_col = col
 
        while matrix[current_row][current_col] == 0:
            matrix[current_row][current_col] = move
            move += 1
 
            for knight_move in knight_moves:
                next_row = current_row + knight_move[0]
                next_col = current_col + knight_move[1]
 
                if next_row >= n or next_row < 0 or next_col >= n or next_col < 0 or matrix[next_row][next_col] != 0:
                    continue
 
                current_row = next_row
                current_col = next_col
                break
 
for row in matrix:
    for cell in row:
        print(cell, end=" ")
    print()
