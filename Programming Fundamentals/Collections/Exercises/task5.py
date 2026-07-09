#Keep names from one collection that are in another collection.

#Example:

# Pesho, Gosho, Tosho, Sasho
# Tosho, Sasho, Misho, Shisho
# output Tosho, Sasho

first_colection = ["Pesho", "Gosho", "Tosho", "Sasho"]
second_colection = ["Misho", "Shisho", "Tosho", "Sasho"]
output = []

for name in first_colection:

    if name in second_colection:
        output.append(name)

print(", ".join(output))
