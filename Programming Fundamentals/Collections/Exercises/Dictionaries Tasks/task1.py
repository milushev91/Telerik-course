# Task 1
# Create a dictionary with pairs for 
# name, age, city.

# Example:

# name -> Alice, age -> 29, city -> London

persons_info = {
    "name": "Alice",
    "age": 29,
    "city": "London",
}

for key, value in persons_info.items():
    print(f"{key} -> {value}", end=", " if value != "London" else "")
