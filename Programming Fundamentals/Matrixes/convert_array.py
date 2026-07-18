array = [num for num in input().split(",")]
rows = int(input())
cols = int(input())

if len(array) != rows * cols:
    print([])
else:
    start = 0
    end = cols
    for _ in range(rows):
        print(" ".join(array[start:end]))
        start = end 
        end += cols
