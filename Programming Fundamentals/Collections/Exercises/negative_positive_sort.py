numbers = input().split()

negatives = []
positives = []

for num in numbers:
    num_int = int(num)
    
    if num_int < 0:
        negatives.append(num)
    else:
        positives. append(num)

sorted_numbers = negatives + positives

print(' '.join(sorted_numbers))
