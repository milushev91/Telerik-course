def extend_output_arr(start, end, arr, add_one):

    for idx in range(start, end):
        number = arr[idx]

        if add_one:
            number += 1
            add_one = False
            
            if number > 9:
                number = int(str(number)[-1])
                add_one = True
            
        output_arr.append(str(number))

first_arr_size, second_arr_size = [int(size) for size in input().split()]
first_arr = [int(num) for num in input().split()]
second_arr = [int(num) for num in input().split()]

        
first_arr_bigger = False
two_digit_sum_num = False

output_arr = []

for idx in range(first_arr_size):
    
    if idx >= second_arr_size:
        first_arr_bigger = True
        break
    
    sum_num = first_arr[idx] + second_arr[idx]
    
    if two_digit_sum_num:
        sum_num += 1
        
        two_digit_sum_num = False
        
    
    if sum_num > 9:
        two_digit_sum_num = True
        
        sum_num = int(str(sum_num)[-1])
    
    
    output_arr.append(str(sum_num))

if first_arr_bigger:
    extend_output_arr(second_arr_size, first_arr_size, first_arr, two_digit_sum_num)
else:
    extend_output_arr(first_arr_size, second_arr_size, second_arr, two_digit_sum_num)

print(" ".join(output_arr))


    
    
    
