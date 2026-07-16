python_dictionary = [ 
    ['word', 'meaning of the word'],
    ['hello', 'hello is a common greeting'],
    ['bye', 'bye is not a common greeting'] 
]

def add_word(word, meaning):
    python_dictionary.append([word, meaning])

def update_meaning(word, meaning):

    for item in python_dictionary:
        
        if item[0] == word:
            item[1] = meaning

def find_word(word):

    for item in python_dictionary:
        if item[0] == word:
            return item[1]
    return None
