card_input = input()

loop_end = 0

if card_input == "J":
    loop_end = 11
elif card_input == "Q":
    loop_end = 12
elif card_input == "K":
    loop_end = 13
elif card_input == "A":
    loop_end = 14
else:
    loop_end = int(card_input)

for card in range(2, loop_end + 1):

    if card == 11:
        card = "J"
    elif card == 12:
        card = "Q"
    elif card == 13:
        card = "K"
    elif card == 14:
        card = "A"

    print(f"{card} of spades, {card} of clubs, {card} of hearts, {card} of diamonds")






 
