# Task 5
# Create a dictionary from n key-value 
# pairs and then print the dictionary.
#  Both n and the key-value pairs are 
#  console inputs.

# Example:

# n = 3
# name:Alice
# city:Sofia
# country:Bulgaria

n = int(input())
person_info = {}

for _ in range(n):
    key, value = input().split(":")
    person_info[key] = value
    
print(person_info)
