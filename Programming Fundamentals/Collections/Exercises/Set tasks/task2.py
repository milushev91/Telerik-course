# Task 2
# Add n elements to a set and print the set. Both n and the elements are console inputs.

# Example:

# a, b, c, d
# n = 4
# e
# f
# g
# a
# a, b, c, d, e, f, g

items = input().split(", ")
n = int(input())

new_set = set(items)

for _ in range(n):
    item = input()
    new_set.add(item)

print(*new_set, sep=", ")
    



