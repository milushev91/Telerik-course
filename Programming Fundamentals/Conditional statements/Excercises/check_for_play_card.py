card = input()

if card.isdigit():
    card = int(card)
    
    if 2 <= card <= 10:
        print("yes")
    else:
        print("no")
else:
    if card == "J" or card == "Q" or card == "A" or card == "K":
        print("yes")
    else:
        print("no")
