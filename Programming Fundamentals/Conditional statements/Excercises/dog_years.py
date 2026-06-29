FIRST_DOG_YEARS = 2

#create constant for first dog years
FIRST_DOG_TO_HUMAN_YEARS = 10

#create constant for rest dog years
NEXT_DOG_TO_HUMAN_YEARS = 4

#read the human years from the console
human_years = int(input())

#create variable for dog years
dog_years = 0

if human_years <= FIRST_DOG_YEARS:
    dog_years = human_years * FIRST_DOG_TO_HUMAN_YEARS
else:
    first_years = FIRST_DOG_YEARS * FIRST_DOG_TO_HUMAN_YEARS
    rest_years = (human_years - FIRST_DOG_YEARS) * NEXT_DOG_TO_HUMAN_YEARS
    dog_years = first_years + rest_years

print(dog_years)
