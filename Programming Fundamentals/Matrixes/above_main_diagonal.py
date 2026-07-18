n = int(input())

matrix = []
sum_above_main_diagonal = 0
for row in range(n):
    row_numbers = [2 ** power for power in range(row, n + row)]
    sum_above_main_diagonal += sum(row_numbers[row + 1::])

print(sum_above_main_diagonal)
