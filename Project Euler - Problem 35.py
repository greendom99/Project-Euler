import math


def check_prime(number):
    for integer in range(2, round(math.sqrt(number)) + 1):
        if number % integer == 0:
            return False
    return True


def number_to_list(number):
    digit_list = []
    for digit in str(number):
        digit_list.append(digit)
    # digit_list = list(map(int, digit_list))
    return digit_list


def even_permutations(digits_list):
    list_permutations = []
    for i in range(0, len(digits_list)):
        perm = [0] * len(digits_list)
        for j in range(0, len(digits_list)):
            if j - i < 0:
                perm[j - i + len(digits_list)] = digits_list[j]
            else:
                perm[j - i] = digits_list[j]
        list_permutations.append(perm)
    return list_permutations


circular_prime = 0
for n in range(2, 1000000):
    for count, permutation in enumerate(even_permutations(number_to_list(n))):
        perm_num = ''
        for digit in permutation:
            perm_num += digit

        if not check_prime(int(perm_num)):
            break
        elif check_prime(int(perm_num)) and count+1 == len(even_permutations(number_to_list(n))):
            circular_prime += 1
print(circular_prime)
