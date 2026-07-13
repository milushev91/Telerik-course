def calculate_letter_points(letter):
    return ord(letter) - 97 + 1

target_number = int(input())
n = int(input())

sum_distance = 0

for _ in range(n):
    word = input()
    letter_distance = 0

    for letter in word:
        letter_distance += calculate_letter_points(letter)
    
    word_distance = abs(letter_distance - target_number)
    sum_distance += word_distance

    print(f"{word} {word_distance}")

print(f"{sum_distance / n:.2f}")
