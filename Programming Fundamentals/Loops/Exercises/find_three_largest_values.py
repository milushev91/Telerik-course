n = int(input())

largest = float("-inf")
second_largest = float("-inf")
third_largest = float("-inf")

for _ in range(n):
    num = int(input())

    if num > largest:
        third_largest = second_largest
        second_largest = largest
        largest = num 
    elif num >= second_largest:
        third_largest = second_largest
        second_largest = num
    elif num >= third_largest:
        third_largest = num

print(f"{largest}, {second_largest} and {third_largest}")




 
