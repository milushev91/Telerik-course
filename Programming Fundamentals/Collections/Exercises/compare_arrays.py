n = int(input())

first_array = []
second_array = []

for _ in range(n):
    num = int(input())
    first_array.append(num)
    
for _ in range(n):
    num = int(input())
    second_array.append(num)

print("equal" if first_array == second_array else "not equal" )
