n = int(input())
prev_num = 0
output = ""

for i in range(n):
    num = int(input())

    if i == 0:
        output += str(num)
    elif num > prev_num:
        output += f"<{num}"
    elif num < prev_num:
        output += f">{num}"
    else:
        output += f"={num}"

    prev_num = num

print(output)
