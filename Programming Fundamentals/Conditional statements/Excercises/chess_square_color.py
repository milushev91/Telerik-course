label = input()
rank = int(input())

light_square_color = "light"
dark_square_color = "dark"

if label == "a" or label == "c" or label == "e" or label == "g":
    if rank % 2 != 0:
        print(dark_square_color)
    else:
        print(light_square_color)
else:
    if rank % 2 != 0:
        print(light_square_color)
    else:
        print(dark_square_color)
