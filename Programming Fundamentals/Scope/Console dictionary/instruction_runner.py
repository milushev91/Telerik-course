import console_dictionary

def execute_instruction(line):
    command, *rest = line.split(":") 
   
    if command == "add":
        word, meaning = rest
        console_dictionary.add_word(word, meaning)

        return f"New word '{word}' was successfully added"
    elif command == "update":
        word, meaning = rest
        console_dictionary.update_meaning(word, meaning)

        return f"Word '{word}'\'s meaning was updated"
    else:
        word = rest[0]
        if console_dictionary.find_word(word):
            for item in console_dictionary.python_dictionary:
        
                if item[0] == word:
                    return "{word}: {item[1]}"
                    
        return "No such word"
