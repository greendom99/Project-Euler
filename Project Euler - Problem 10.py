import math


def test_prime(number):
    for n in range(2, round(math.sqrt(number)) + 1):
        if number % n == 0:
            return False
    return True


# number of primes want to find
prime_sum = 0

for i in range(2, 2000000):
    if test_prime(i):
        prime_sum += i
print(prime_sum)
