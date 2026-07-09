# Keep names from one collection that 
# are not in another collection.

# Example:

# Pesho, Gosho, Tosho, Sasho
# Tosho, Sasho, Misho, Shisho
# output Pesho, Gosho

first_colection = ["Pesho", "Gosho", "Tosho", "Sasho"]
second_colection = ["Misho", "Shisho", "Tosho", "Sasho"]
output = []

for name in first_colection:

    if name not in second_colection:
        output.append(name)

print(", ".join(output))
