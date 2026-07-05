temperatures = input().split()

for temp in temperatures:
    farenheit = round(int(temp) * 9/5 + 32)
    print(farenheit)
