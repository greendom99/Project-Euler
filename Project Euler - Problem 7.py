import math


def test_prime(number):
    for n in range(2, round(math.sqrt(number)) + 1):
        if number % n == 0:
            return False
    return True


# number of primes want to find
prime_count = 1
max_prime_count = 10001
count = 2

while prime_count <= max_prime_count:
    if test_prime(count):
        prime_count += 1
    count = count + 1
print(count-1)