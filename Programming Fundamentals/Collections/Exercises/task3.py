# Task 3
# Calculate the average score of tournament 
#participants (single line console input).

# Example:

# Pesho:9, Gosho:7, Tosho:8, Sasho:4, Pesho:6, Pesho:9, Tosho:9, Gosho:10, Tosho:6, Tosho:7, Sasho:5, Sasho:6, Sasho:10, Sasho:3, Misho: 9
# output Pesho -> 8.0, Gosho -> 8.5, Tosho -> 7.5, Sasho -> 5.6, Misho -> 9.0

lines = input().split(", ")
scores = {}

for line in lines:
    name, score = line.split(":")

    if name not in scores:
        scores[name] = 0

    scores[name] += int(score)
    
for key, value in scores.items():
    print(f"{key} -> {value}", end=" ")







