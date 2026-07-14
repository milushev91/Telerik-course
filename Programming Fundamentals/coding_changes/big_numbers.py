n1, n2 = [int(n) for n in input().split()]
first_array = [int(num) for num in input().split()]
second_array = [int(num) for num in input().split()]

arrays_len = {
    len(first_array): first_array,
    len(second_array): second_array
}

lengths = arrays_len.keys()

min_len, max_len = min(lengths), max(lengths)
sum_array = [0] * max_len
additions = [0] * max_len

for idx in range(min_len):
    current_sum = first_array[idx] + second_array[idx]

    if current_sum > 9:
        current_sum = str(current_sum)[-1]

        if idx != (max_len - 1):
            additions[idx + 1] += 1
        else:
            additions[idx] += 1
    
    
    sum_array[idx] += int(current_sum)


for idx in range(max_len - 1, min_len - 1, -1):
    sum_array[idx] = arrays_len[max_len][idx]

print(sum_array)



    
    
    
