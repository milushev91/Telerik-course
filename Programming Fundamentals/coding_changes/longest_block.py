input_ = input()

largest_block = ""
current_block = ""

for char in input_:
    if not current_block or char == current_block[-1]:
        current_block += char
    else:
        current_block = char

    if len(current_block) > len(largest_block):
        largest_block = current_block

print(largest_block)
