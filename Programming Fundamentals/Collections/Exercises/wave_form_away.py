line = [int(el) for el in input().split()]
output = ""
el_0 = line[0]

for el in line[1:]:

    if el > el_0:
        output += "+"
    else:
        output += "-"
    
    el_0 = el
   
if "--" in output or "++" in output:
    print("no")
else:
    print("yes")
print(output)
