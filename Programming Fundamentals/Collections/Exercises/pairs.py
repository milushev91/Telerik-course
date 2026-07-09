number = int(input())
numbers = [int(num) for num in input().split()]
numbers_len = len(numbers)
has_pairs = False

for i in range(numbers_len - 1):
    first_num = numbers[i]

    for j in range(i + 1, numbers_len):
        second_num = numbers[j]

        if number == first_num + second_num:
            print(f"{first_num},{second_num}")
            has_pairs = True 

if not has_pairs:
    print("no pairs")


    
