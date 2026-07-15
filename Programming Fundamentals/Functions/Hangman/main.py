def get_word():
    word = input("Guess a word: ").lower()

    while not word.isalpha():
        print("Your guess should contain only letters!wo")
        word = input("Guess a word:").lower()
    
    return word


def get_initial_positions(word_len):
    initial_positions = []

    for idx in range(word_len):
        if idx == 0 or idx == word_len - 1:
            initial_positions.append(True)
        else:
            initial_positions.append(False)
    
    return initial_positions


def hide_word(word, guessed_positions):
    word_len = len(word)
    hidden_word = []

    for idx in range(word_len):
        if guessed_positions[idx]:
            hidden_word.append(word[idx])
        else:
            hidden_word.append("-")
    
    return "".join(hidden_word)

def check_guess(word, letter, positions):
    new_positions = positions.copy()

    for idx in range(len(word)):
        if word[idx] == letter:
            new_positions[idx] = True
    
    return new_positions
        
def check_for_win(positions):
    return len(set(positions)) == 1

def play_hangman():
    word = get_word() # use the 'get_word' function here
    lives = 5 # choose some initial number of lives
    positions = get_initial_positions(len(word)) # use the 'get_initial_positions' function. 
    hidden = hide_word(word, positions) # use the 'hide_word' function here to create  the initially hidden word. The function should work with the 'word' and 'positions' variables
     
    print(hidden)
     
    while True: # we will check for win or loss in the loop and break accordingly
        next_letter = input()
        new_positions = check_guess(word, next_letter, positions)# use the check_guess function here. Pass the correct arguments to it.
     
        # Option 1 - both lists are the same - the next_letter is not a correct guess
        if new_positions == positions:
            print('No such letter or already guessed')
            print(f'Lives remaining: {lives - 1}')
            lives = lives - 1
     
            if lives == 0: # no more lives - break
                print('You lose!')
                break
     
        # Option 2 - if the lists are not the  same, all values in new_positions may be True
        #    we use the check_for_win function to validate
        elif check_for_win(new_positions):
            print('You win!')
            break
     
        # Option 3 - the two lists are not the same, and new_postions is not all True - this means that another letter is guessed. We need to print it.
        else:
            print('Another letter guessed!')
            print(hide_word(word, new_positions))# use the hide_word again, but this time with new_positions
     
            # it's important to update the positions list for the next iteration
            positions = new_positions 

play_hangman()

