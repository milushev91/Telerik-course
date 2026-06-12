num = int(input())


ones = num % 10
tens = str(123 % 100)[0]
hundreds = 123 // 100


print(f"{hundreds}{tens}{ones}")
