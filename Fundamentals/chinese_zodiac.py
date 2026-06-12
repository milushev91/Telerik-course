BASE_YEAR = 2000
CYCLES = 12

year = int(input())

year_index = (year - BASE_YEAR) % CYCLES

if year_index == 0:
    print("Dragon")
elif year_index == 1:
    print("Snake")
elif year_index == 2:
    print("Horse")
elif year_index == 3:
    print("Sheep")
elif year_index == 4:
    print("Monkey")
elif year_index == 5:
    print("Roaster")
elif year_index == 6:
    print("Dog")
elif year_index == 7:
    print("Pig")
elif year_index == 8:
    print("Rat")
elif year_index == 9:
    print("Ox")
elif year_index == 10:
    print("Tiger")
else:
    print("Hare")
