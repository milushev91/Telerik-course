fruits = ["apple", "banana", "cherry", "banana", "apple", "apple", "banana"]

fruit_counts = {}

for fruit in fruits:
    if fruit not in fruit_counts:
        fruit_counts[fruit] = 0
    
    fruit_counts[fruit] += 1 

print(f"{len(fruit_counts)} of unique words")

for key, value in fruit_counts.items():
    print(f"{key} -> {value}")
