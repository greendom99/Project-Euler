import math
import itertools

# returns true/false if number is/not prime.
def check_prime(number):
    if number < 2:
        return False
    for integer in range(2, round(math.sqrt(number)) + 1):
        if number % integer == 0:
            return False
    return True


# returns a list of all permutations of digits 1 to n
def perm_number(n):
    digits = []
    for integer in range(1, n+1):
        digits.append(integer)

    perm_list = []
    for perm in list(itertools.permutations(digits)):
        number = ''
        for digit in perm:
            number += str(digit)
        perm_list.append(int(number))
    return perm_list


max_pan_prime = 0
for i in range(1, 10):
    for permutation in perm_number(i):
        if check_prime(permutation):
            if permutation > max_pan_prime:
                max_pan_prime = permutation
print(max_pan_prime)
