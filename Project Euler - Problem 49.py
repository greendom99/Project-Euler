import math
import itertools


def check_prime(number):
    if number < 2:
        return False
    for integer in range(2, round(math.sqrt(number)) + 1):
        if number % integer == 0:
            return False
    return True


def prime_perm_generator(digit_list):
    perm_list = list(itertools.permutations(digit_list))
    prime_perm_list = []
    for perm in perm_list:
        num = ''
        for digit in perm:
            num += str(digit)
        if num[0] == '0':
            continue
        else:
            if check_prime(int(num)):
                prime_perm_list.append(int(num))
    return prime_perm_list


def condition_check(pp_list):
    for i in range(0, len(pp_list)):
        for j in range(i + 1, len(pp_list)):
            for k in range(j + 1, len(pp_list)):
                if pp_list[j] - pp_list[i] == pp_list[k] - pp_list[j] and pp_list[k] - pp_list[j] != 0:
                    return pp_list[i], pp_list[j], pp_list[k]


def search():
    for a in range(0, 10):
        for b in range(0, 10):
            for c in range(0, 10):
                for d in range(0, 10):
                    if condition_check(prime_perm_generator([a, b, c, d])) is not None:
                        n_1, n_2, n_3 = condition_check(prime_perm_generator([a, b, c, d]))
                        if n_1 != 1487:
                            return str(n_1) + str(n_2) + str(n_3)


print(search())
