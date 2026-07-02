target_number = int(input())
n = int(input())

alphabet = "abcdefghijklmnopqrstuvwxyz"
sum_distance = 0

for _ in range(n):
    word = input()
    word_char_sum = 0
    
    for char in word:
        word_char_sum += alphabet.index(char) + 1
    
    word_distance = abs(target_number - word_char_sum)
    sum_distance += word_distance
    print(f"{word} {word_distance}")

avg_distance = sum_distance / n 

print(f"{avg_distance:.2f}")
