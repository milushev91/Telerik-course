# 2. Write a function that returns 
# the largest number from a given list of numbers, 
# without using the build-in function max.

def find_largest(numbers): 
    largest_number = float("-inf")

    for num in numbers:
        if num > largest_number:
            largest_number = num
    
    return largest_number

x = find_largest([1, 2, 3, 4, 5])  # largest should be 5
print(x)
x = find_largest([-10, -2, -3, -6])  # largest should be -2
