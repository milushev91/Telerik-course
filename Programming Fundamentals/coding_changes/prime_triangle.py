def check_prime(number):

    if number == 1:
        return True

    for num in range(2, number):
        if number % num == 0:
            return False 
    
    return True

n = int(input())

for num in range(1, n + 1):

    if check_prime(num):

        for line_number in range(1, num + 1):
            if check_prime(line_number):
                print(1, end="")
            else:
                print(0, end="")
        print()
