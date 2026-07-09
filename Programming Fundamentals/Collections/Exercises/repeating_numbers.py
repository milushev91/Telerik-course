n = int(input())

num_info = {}

for _ in range(n):
    num = input()

    if num not in num_info:
        num_info[num] = 0
    
    num_info[num] += 1

most_repeated_counter = 0
most_repeated_number = 0

for key, value in num_info.items():

    if value > most_repeated_counter:
        most_repeated_counter = value
        most_repeated_number = key 
    elif value == most_repeated_counter:
        most_repeated_number = key if int(key) < int(most_repeated_number) else most_repeated_number

print(int(most_repeated_number))
    
