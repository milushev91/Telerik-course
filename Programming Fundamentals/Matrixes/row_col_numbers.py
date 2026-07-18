matrix = [[int(num) for num in line.split()] for line in input().split(",")]
n = len(matrix[0])
required_numbers = [num for num in range(1, n + 1)]

for row in range(n):
    col_numbers = []

    for idx in range(n):
        col_numbers.append(matrix[idx][row])
    
    sorted_col = sorted(col_numbers)
    sorted_row = sorted(matrix[row])
    
    if sorted_row != required_numbers or sorted_col != required_numbers:
        print("false")
        break 
     
else:
    print("true")
