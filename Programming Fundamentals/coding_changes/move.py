position = int(input())
field = [int(num) for num in input().split(",")]
field_len = len(field)

forward_score = backwards_score = 0

line = input()

while line != "exit":
    steps, command, size = [int(item) if item[-1].isdigit() else item for item in line.split()]
    
    if command == "forward":
        for _ in range(steps):
            position = (position + size) % field_len
            forward_score += field[position]
    else:
        for _ in range(steps):
            position = (position - size) % field_len
            backwards_score += field[position]
            
    line = input()
  
print(f"Forward: {forward_score}")
print(f"Backwards: {backwards_score}")
