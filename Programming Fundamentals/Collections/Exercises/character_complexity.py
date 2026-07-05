first_word = input()
second_word = input()

first_word_len = len(first_word)
second_word_len = len(second_word)
smaller_len = min(first_word_len, second_word_len)

for i in range(smaller_len):
    
    if first_word[i] < second_word[i]:
        print("first")
        break
    elif first_word[i] > second_word[i]:
        print("second")
        break
else:
    if first_word_len == second_word_len:
        print("equal")
    elif second_word_len > first_word_len:
        print("first")
    else:
        print("second")
