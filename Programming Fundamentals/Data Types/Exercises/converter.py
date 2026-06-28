kilometers = 100
gallon = 4.54
mile = 1.6

miles_per_gallon = int(input())

# calculate km per gallon
kms_per_gallon = miles_per_gallon * mile

# divide kilometers by multiplication
# of kms per gallon by gallon litters
spent_litters = kilometers / kms_per_gallon * gallon
# print floored result
print(f"{int(spent_litters)} litres per 100 km")
