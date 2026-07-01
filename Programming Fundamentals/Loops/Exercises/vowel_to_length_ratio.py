#read number of words
words_count = int(input())

# variables
vowels = 'aouei'
winning_word = None
winning_word_ratio = None
winning_word_vowels = 0
winning_word_len = 0

# loop number of words times
for _ in range(words_count):
    # read word
    word = input()

    word_vowels = 0
    word_len = len(word)
    
    # loop through every char of word 
    for char in word:
        # char in vowels string
        if char in vowels:
            word_vowels += 1
            
    # calculate word ratio 
    word_ratio = word_vowels / word_len

    # check word ratios is less than winning_word_ratio
    if not winning_word or word_ratio < winning_word_ratio:
        # set word as winning 
        winning_word = word
        winning_word_vowels = word_vowels
        winning_word_ratio = word_ratio
        winning_word_len = word_len

    # check word ratios is equal to winning_word_ratio
    elif word_ratio == winning_word_ratio:
        #set word with more vowels as winning
        if word_vowels > winning_word_vowels or (word_vowels == winning_word_vowels and word_len > winning_word_len):
            winning_word = word
            winning_word_vowels = word_vowels
            winning_word_ratio = word_ratio
            winning_word_len = word_len

print(f"{winning_word} {winning_word_vowels}/{winning_word_len}")
