n = int(input())

longest_seq = []
seq = []

for _ in range(n):
    num = int(input())
  
    if not seq: 
        seq.append(num)
    else:

        if seq[-1] < num:
            seq.append(num)

            if len(seq) > len(longest_seq):
                longest_seq = seq.copy()
        else:
            seq = [num]

print(len(longest_seq))


        


