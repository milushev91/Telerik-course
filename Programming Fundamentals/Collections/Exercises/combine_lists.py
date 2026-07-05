first_list = input().split(",")
second_list = input().split(",")

output_list = []
first_list_len = len(first_list)


for i in range(first_list_len):
    output_list.append(first_list[i])
    output_list.append(second_list[i])

print(','.join(output_list))
