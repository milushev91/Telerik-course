half_litter_bottles = int(input())
litter_bottles = int(input())

half_litter_bottles_deposit = half_litter_bottles * 0.1
litter_bottles_deposit = litter_bottles * 0.25

deposit = half_litter_bottles_deposit + litter_bottles_deposit

print(f"{deposit:.2f}")
