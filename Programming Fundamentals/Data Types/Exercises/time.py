d = int(input())
h = int(input())
m = int(input())
s = int(input())

hours = d * 24 + h

minutes = m + hours * 60 
seconds = s + minutes * 60

print(seconds)
