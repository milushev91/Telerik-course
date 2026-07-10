# Task 4
# Keep all values, except the last one, from a
# single line of input with unknown amount of values.

# Example:

# input Pesho Gosho Tosho
# output Pesho, Gosho
# input Pesho Gosho Tosho Sasho Misho
# output Pesho, Gosho, Tosho, Sasho
# input Pesho
# output 

names = input().split()

print(' '.join(names[:len(names) -1]))
