def check_prime(num):
    if num <= 1:
        return False 
    
    for i in range(2, num):
        if num % i == 0:
            return False 
    
    return True

matrix = [line for line in input().split(",")]
largest_prime = 0
matrix_size = len(matrix)

for row in range(matrix_size):
    row_numbers = [int(num) for num in matrix[row].split()]
    left_diagonal_num = row_numbers[row]
    right_diagonal_num  = row_numbers[matrix_size - 1 - row]

    if check_prime(left_diagonal_num):
        if left_diagonal_num > largest_prime:
            largest_prime = left_diagonal_num
    
    if check_prime(right_diagonal_num):
        if right_diagonal_num > largest_prime:
            largest_prime = right_diagonal_num

print(largest_prime)



