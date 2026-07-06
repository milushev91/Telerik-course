# Task 4
# Append n elements to a list and print the list. Both n and the elements are console inputs.

# Example:

# n = 4
# 1
# 2
# 3
# 4
# [1, 2, 3, 4]

n = int(input())

numbers = []

for _ in range(n):
    numbers.append(int(input()))

print(numbers)
