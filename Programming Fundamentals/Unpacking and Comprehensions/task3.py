# Task 3
# Declare three variables on a single line from a 
# single line console input with three or more values.

# Example:

# input Pesho Gosho Tosho friends
# output Hi, my name is Pesho. Gosho, Tosho are my friends.
# input Pesho Gosho Tosho Sasho family
# output Hi, my name is Pesho. Gosho, Tosho, Sasho are my family.

name, *names,  relation = input().split()

print(f"Hi, my name is {name}. {', '.join(names)} are my {relation}.")
