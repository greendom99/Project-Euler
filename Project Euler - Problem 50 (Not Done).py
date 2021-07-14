import math


def check_prime(number):
    if number < 2:
        return False
    for integer in range(2, round(math.sqrt(number)) + 1):
        if number % integer == 0:
            return False
    return True


N = 1000
prime_list = []
for n in range(1, N):
    if check_prime(n):
        prime_list.append(n)

max_length_found = 0
max_sum_found = 0
for i in range(0, len(prime_list)):
    sum_primes = 0
    primes = []

    for j in range(i, len(prime_list)-1):
        print(prime_list[j])
        sum_primes += prime_list[j]
        primes.append(prime_list[j])
        if check_prime(sum_primes) and sum_primes + prime_list[j+1] < N:
            if len(primes) > max_length_found:
                store_primes = primes.copy()
                max_length_found = len(primes)
                max_sum_found = sum_primes
        elif not check_prime(sum_primes) and sum_primes + prime_list[j+1] < N:
            continue
        else:
            break


print("answer is", store_primes, len(store_primes), max_sum_found)
