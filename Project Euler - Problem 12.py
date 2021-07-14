import math


def find_triangle_num(n):
    triangle_num = 0
    for i in range(1, n + 1):
        triangle_num += i
    return triangle_num


def find_factors(number):
    factors = [1, number]
    for i in range(2, round(math.sqrt(number)) + 1):
        if number % i == 0:
            factors.append(i)
            factors.append(int(number / i))
    factors = list(dict.fromkeys(factors))
    factors.sort()
    return factors


z = 0
answer = 0
while z != -1:
    z = z + 1
    triangle_factors = find_factors(find_triangle_num(z))
    if len(triangle_factors) > 500:
        answer = find_triangle_num(z)
        z = -1
print(answer)
