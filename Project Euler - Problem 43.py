import itertools

primes = [2, 3, 5, 7, 11, 13, 17]

# returns a list of all permutations of digits 1 to n
def perm_number(n):
    digits = []
    for integer in range(0, n + 1):
        digits.append(integer)

    perm_list = []
    for perm in list(itertools.permutations(digits)):
        number = ''
        for digit in perm:
            number += str(digit)
        # remove numbers with leading 0
        if number[0] != '0':
            perm_list.append(int(number))
    return perm_list


def check_property(number):

    for i in range(2, 9):
        if int(number[i-1] + number[i] + number[i + 1]) % primes[i-2] != 0:
            return False
    return True


list_numbers = perm_number(9)
sum_answer = 0
for n in list_numbers:
    if check_property(str(n)):
        sum_answer += n
print(sum_answer)

