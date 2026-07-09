# Task 8
# Remove values (console inputs) if they appear more
# than once in a collection.

# Example:

# Pesho, Pesho, Pesho, Gosho, Gosho, Tosho, Sasho, Sasho
# Pesho
# Pesho
# Pesho
# Gosho
# Gosho
# Tosho
# end
# output Pesho, Gosho, Tosho, Sasho, Sasho

collection = ["Pesho", "Pesho", "Pesho", "Gosho", "Gosho", "Tosho", "Sasho", "Sasho"]

command = input()

while command != "end":
    name = command

    if collection.count(name) > 1:
        collection.remove(name)

    command = input()

print(", ".join(collection))



