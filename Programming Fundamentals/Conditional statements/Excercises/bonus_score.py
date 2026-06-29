score = int(input())

if 1 <= score <= 3:
    print(score * 10)
elif 4 <= score <= 6:
    print(score * 100)
elif 7 <= score <= 9:
    print(score * 1000)
else:
    print("invalid score")
