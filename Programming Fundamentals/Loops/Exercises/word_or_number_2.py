n = int(input())

words = "no words"
sum_numbers = "0"

for _ in range(n):
    line = input()

    if line.isdigit():

        if sum_numbers == "0":
            sum_numbers = int(sum_numbers) + int(line)
        else:
            sum_numbers += int(line)
    else:
        
        if words == "no words":
            words = line 
        else:
            words += f"-{line}"

print(words)
print(sum_numbers)
