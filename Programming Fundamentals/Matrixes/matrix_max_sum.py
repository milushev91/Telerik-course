n = int(input())

matrix = [[int(num) for num in input().split()] for _ in range(n)]
print(*matrix, sep="\n")
cordinate_line = [int(num) for num input().split()]
cordinate_line_len = len(cordinate_line)
cordinate_pairs = [cordinate_line[end-2:end] for end in range(2, cordinate_line_len)]
print(cordinate_pairs)
