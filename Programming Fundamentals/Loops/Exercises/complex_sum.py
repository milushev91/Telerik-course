n = int(input())
x = float(input())
 
temp = 1 
sum_nums = temp 
 
for i in range(1, n+1): 
    temp = (temp * i) 
    sum_nums += temp / x ** i 
 
print(f"{sum_nums:.5f}")
