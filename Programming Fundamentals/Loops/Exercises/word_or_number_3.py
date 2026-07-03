def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


n = int(input())

prev = input()

if prev.isalpha():
    current_type = "word"
    words = prev
    num_sum = 0
elif is_number(prev):
    current_type = "number"
    num_sum = int(prev)
    words = ""
else:
    current_type = "other"

for _ in range(1, n):
    line = input()

    if line.isalpha():
        line_type = "word"
    elif is_number(line):
        line_type = "number"
    else:
        line_type = "other"

    if current_type == "word" and line_type == "word":
        words += "-" + line

    elif current_type == "number" and line_type == "number":
        num_sum += int(line)

    else:
        # Print the completed group
        if current_type == "word":
            print(words)
        elif current_type == "number":
            print(num_sum)
        else:
            print(prev)

        # Start a new group
        if line_type == "word":
            words = line
        elif line_type == "number":
            num_sum = int(line)

        current_type = line_type

    prev = line

# Print the final group
if current_type == "word":
    print(words)
elif current_type == "number":
    print(num_sum)
else:
    print(prev)
