# 4 3 2 5 2
# 0 2 4 6 8

n = int(input())
numbers = input()

numbers_len = len(numbers)
even = odd = 1
counter = 0

for i in range(0, numbers_len + 1, 2):
    current_number = int(numbers[i])

    if counter % 2 == 0:
        odd *= current_number
    else:
        even *= current_number

    counter += 1

if even == odd:
    print(f"yes {even}")
else:
    print(f"no {odd} {even}")
