import math

list_primes = []


def is_prime(num):
    if num <= 1:
        return False
    factors = [1, num]
    for integer in range(2, round(math.sqrt(num)) + 1):
        if num % integer == 0:
            factors.append(n)
            factors.append(int(num / integer))
    if len(factors) == 2:
        return True
    else:
        return False


max_prime_count = 0
answer = 0
for a in range(-999, 1000):
    for b in range(2, 1001):
        prime_count = 0
        z = 0
        n = 0
        while z == 0:
            if is_prime(n ** 2 + a * n + b):
                prime_count += 1
                n += 1
            else:
                if prime_count > max_prime_count:
                    max_prime_count = prime_count
                    answer = a * b
                z = 1
print(answer)
