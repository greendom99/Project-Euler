import math


def check_prime(number):
    if number<2:
        return False
    for integer in range(2, round(math.sqrt(number)) + 1):
        if number % integer == 0:
            return False
    return True

def trunc_left_to_right(number):
    for integer in range(0, len(str(number))):
        num = str(number)[integer:]
        if not check_prime(int(num)):
            return False
    return True

def trunc_right_to_left(number):
    for integer in range(0, len(str(number))):
        if integer != 0:
            num = str(number)[:-integer]
        else:
            num = number
        if not check_prime(int(num)):
            return False
    return True


trunc_prime_sum = 0
prime_count = 0
ticker = 8

while prime_count < 11:
    if trunc_left_to_right(ticker) and trunc_right_to_left(ticker):
        trunc_prime_sum += ticker
        prime_count += 1
    ticker += 1
print(trunc_prime_sum)
