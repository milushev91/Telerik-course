# Write a function that determines if three numbers (representing lengths of sides)
#  can form a triangle. To form a triangle the largest side must be smaller than the sum of
#   the other two. You do not know which of the three parameters will be the largest.

def can_form_triangle(*args):
    sum_args = sum(args)
    max_args = max(args)
    return (sum_args - max_args) > max_args


x = can_form_triangle(3,4,5) # x = True
print(x)
x = can_form_triangle(3,6,3) # x = False
print(x)
