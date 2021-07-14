import math


def check_prime(number):
    if number < 2:
        return False
    for integer in range(2, round(math.sqrt(number)) + 1):
        if number % integer == 0:
            return False
    return True


def check_composite(number):
    if number != 1 and not check_prime(number):
        return True
    else:
        return False


def check_perfect_square(number):
    if int(math.sqrt(number) + 0.5) ** 2 == number:
        return True
    else:
        return False


# generate primes
primes = []
for i in range(1, 10000):
    if check_prime(i):
        primes.append(i)


def conjecture_check(comp_num):
    z = 0
    for prime in primes:
        if prime < comp_num:
            if check_perfect_square(int((comp_num - prime) / 2)):
                z = 1
    if z != 0:
        return True
    else:
        return False


def main():
    n = 1
    while True:
        if n % 2 == 1 and check_composite(n):
            if not conjecture_check(n):
                return n
        n = n+1


print(main())
