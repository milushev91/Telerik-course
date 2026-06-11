input_type = input()
value = input()

if input_type == "integer":
    print(int(value) + 1)
elif input_type == "real":
    print(f"{float(value) + 1:.2f}")
else:
    print(value)
