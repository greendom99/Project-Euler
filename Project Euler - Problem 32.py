import math


def find_factors(num):
    factors = [1]
    for n in range(2, round(math.sqrt(num)) + 1):
        if num % n == 0:
            factors.append(n)
            factors.append(int(num / n))
    factors.sort()
    return list(dict.fromkeys(factors))

def check_pandigital(number):
    digits = []
    check_digits = []

    for value, digit in enumerate(str(number)):
        digits.append(value+1)
        check_digits.append(int(digit))
    check_digits.sort()
    check_digits = list(dict.fromkeys(check_digits))

    if digits == check_digits:
        return True
    else:
        return False


list_answers = []

for N in range(1, 10000):
    for factor in find_factors(N):
        a = factor
        b = int(N/factor)
        if a <= b:
            c = str(a) + str(b) + str(N)
            if check_pandigital(c) and len(c) == 9:
                list_answers.append(N)

list_answers = list(dict.fromkeys(list_answers))

answer_sum = 0
for answer in list_answers:
    answer_sum += answer
print(answer_sum)
