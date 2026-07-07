# Task 2
# Calculate the total score of tournament participants (console input).

# Example:

# Pesho:9
# Gosho:7
# Tosho:8
# Sasho:4
# Pesho:6
# Pesho:9
# Gosho:9
# Gosho:10
# Tosho:6
# Tosho:7
# Sasho:5
# Sasho:6
# end
# output Pesho -> 24, Gosho -> 26, Tosho -> 21, Sasho -> 15

scores = {}

command = input()

while command != "end":
    name, score = command.split(":")

    if name not in scores:
        scores[name] = 0

    scores[name] += int(score)

    command = input()
    
for key, value in scores.items():
    print(f"{key} -> {value}")
