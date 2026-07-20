rows = int(input())

matrix = [list(map(int, input().split())) for _ in range(rows)]

coords = list(map(int, input().split()))

cols = len(matrix[0])

max_sum = float('-inf')

for i in range(0, len(coords), 2):
    r = coords[i]
    c = coords[i + 1]

    row = abs(r) - 1
    col = abs(c) - 1

    current_sum = 0

    # Horizontal movement
    if r > 0:
        # Start from the left
        for j in range(col + 1):
            current_sum += matrix[row][j]
    else:
        # Start from the right
        for j in range(cols - 1, col - 1, -1):
            current_sum += matrix[row][j]

    # Vertical movement
    if c > 0:
        # Move up
        for rr in range(row - 1, -1, -1):
            current_sum += matrix[rr][col]
    else:
        # Move down
        for rr in range(row + 1, rows):
            current_sum += matrix[rr][col]

    max_sum = max(max_sum, current_sum)

print(max_sum)
