start = int(input())
end = int(input())
target = int(input())

for num in range(start, end + 1):
    num_str = str(num)
    digit_sum = 0

    for digit in num_str:
        digit_sum += int(digit)
    
    if digit_sum == target:
        print(num)
