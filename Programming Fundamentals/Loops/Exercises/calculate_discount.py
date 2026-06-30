DISCOUNT_PERCENT = 0.35

n = int(input())

for i in range(n):
    item_price = float(input())

    print(f"{item_price * DISCOUNT_PERCENT:.2f}")
