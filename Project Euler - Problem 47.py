import math


def count_distinct_prime_factors(n):
    count = 0
    while n > 1:
        count += 1
        for i in range(2, round(math.sqrt(n) + 1)):
            if n % i == 0:
                while True:
                    n //= i
                    if n % i != 0:
                        break
                break
        else:
            break  # n is prime
    return count


def search(max_length):
    number_list = [2]
    for n in range(3, 1000000):

        count_dpf = count_distinct_prime_factors(n)
        if number_list == [] and count_dpf == max_length:
            number_list.append(n)
            continue
        elif number_list == [] and count_dpf != max_length:
            continue
        else:
            z = 0

        if count_dpf == max_length and n == number_list[-1] + 1:
            number_list.append(n)
            if len(number_list) == max_length:
                return number_list
        elif count_dpf == max_length:
            number_list = [n]
        else:
            number_list = []


N = 4
answer = search(N)[0]
print(answer)
