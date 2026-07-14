# 4. Write a function generate_password 
# that creates a simple, random password 
# consisting of letters and digits.
#  You will need to find out how "random" works.
from random import randint

def generate_password(length):
    password = ""

    for idx in range(1, length + 1):

        if idx % 3 == 0:
            password += str(randint(0, 9))
        else:
            random_index = randint(0, 1)
            random_numbers = [randint(65, 90), randint(97,122)]
            password += chr(random_numbers[random_index])

    return password


x = generate_password(8)  # password could be "aB3dE4fG"
print(x)
# x = generate_password(12) # password could be "Hk9Pv4wBz2Lq"




    
    
    
