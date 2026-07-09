# Task 7
# Search in a collection based on a car make or
# model (console input) and return the opposite.

# Example:

# Honda -> Civic, Accord
# Ford -> Fiesta, Focus
# Volkswagen -> Golf, Passat
# input Focus
# output Ford
# input Ford
# output Fiesta, Focus

cars = {
    "Honda": ["Civic", "Accord"],
    "Ford": ["Fiesta", "Focus"],
    "Volkswagen": ["Golf", "Passat"],
}

input_ = input()

for key, values in cars.items():

    if input_ == key:
        print(', '.join(values))
        break
    elif input_ in values:
        print(key)
        break
