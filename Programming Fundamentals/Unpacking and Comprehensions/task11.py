# Task 11
# Write a comprehension that keeps only the values that are greater than
# the average of all the values.

# Example:

# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# [6, 7, 8, 9, 10]

numbers = [int(num) for num in input().split(", ")]
avg_numbers = sum(numbers) / len(numbers)

filtered_numbers = [num for num in numbers if num > avg_numbers]

print(filtered_numbers)
