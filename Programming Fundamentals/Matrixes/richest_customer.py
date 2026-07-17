# 1 2 3
# 3 2 1
max_account_sum = 0

line = input()

while line:
    current_account_sum = sum(int(num) for num in line.split())
    
    if current_account_sum > max_account_sum:
        max_account_sum = current_account_sum
    
    line = input()

print(max_account_sum)
    
