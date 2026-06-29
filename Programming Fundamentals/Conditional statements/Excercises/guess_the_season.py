month = input()
day = int(input())

season = None

if month == "January" or month == "February":
    season = "Winter"
elif month == "March":
    if day < 20:
        season = "Winter"
    else:
        season = "Spring"
elif month == "April" or month == "May":
    season = "Spring"
elif month == "June":
    if day < 21:
        season = "Spring"
    else:
        season = "Summer"
elif month == "July" or month == "August":
    season = "Summer"
elif month == "September":
    if day < 22:
        season = "Summer"
    else:
        season = "Autumn"
elif month == "October" or month == "November":
    season == "Autumn"
else:
    if day < 21:
        season = "Autumn"
    else:
        season = "Winter"

print(season)
