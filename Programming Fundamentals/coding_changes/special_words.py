words = [word for word in input().split()]

unique_words = {}

for word in words:
    sorted_word = sorted(word)

    if sorted_word not in unique_words.values():
        unique_words[word] = sorted_word

print(" ".join(unique_words.keys()))
