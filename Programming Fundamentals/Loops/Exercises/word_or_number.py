def is_int(element):
    try:
        int(element)
        return True
    except ValueError:
        return False

def is_float(element):
    try:
        float(element)
        return True
    except ValueError:
        return False

input_ = input()

if is_int(input_):
    print(int(input_) + 1)
elif is_float(input_):
    print(float(input_) + 1)
else:
    word_len = len(input_)

    for i in range(word_len - 1, -1, -1):
        print(input_[i], end="")
