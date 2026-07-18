rows, cols = [int(num) for num in input().split()]

max_ones_counter = 0
max_ones_index = 0

for row in range(rows):
    row_numbers = [int(num) for num in input().split()]
    row_ones_counter = 0
    
    for col in range(cols):
        if row_numbers[col] == 1:
            row_ones_counter += 1 

    if row_ones_counter > max_ones_counter:
        max_ones_counter = row_ones_counter
        max_ones_index = row

print(f"{max_ones_index},{max_ones_counter}")
