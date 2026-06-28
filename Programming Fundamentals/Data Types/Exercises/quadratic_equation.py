import math

a = float(input())
b = float(input())
c = float(input())

D = b*b - 4*a*c

x1 = (-b - math.sqrt(D)) / (2*a)
x2 = (-b + math.sqrt(D)) / (2*a)

# Format removes the negative sign from -0.0
print("x1={:.1f}".format(x1).replace("-0.0", "0.0"))
print("x2={:.1f}".format(x2).replace("-0.0", "0.0"))
