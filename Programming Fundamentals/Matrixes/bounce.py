rows, cols = map(int, input().split())

if rows == 1 or cols == 1:
    print(1)
else:
    row = 0
    col = 0

    row_dir = 1
    col_dir = 1

    sum_score = 1 

    while True:
        row += row_dir
        col += col_dir

        sum_score += 2 ** (row + col)

        # Stop when another corner is reached
        if (row == 0 or row == rows - 1) and \
           (col == 0 or col == cols - 1):
            break

        # Bounce vertically
        if row == 0 or row == rows - 1:
            row_dir *= -1

        # Bounce horizontally
        if col == 0 or col == cols - 1:
            col_dir *= -1

    print(sum_score)
