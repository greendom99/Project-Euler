import math

number = 220


def find_factors(num):
    factors = [1]
    for n in range(2, round(math.sqrt(num)) + 1):
        if num % n == 0:
            factors.append(n)
            factors.append(int(num / n))
    factors.sort()
    return list(dict.fromkeys(factors))


def sum_factors(factors):
    sum_fact = 0
    for fact in factors:
        sum_fact += fact
    return sum_fact


amicable_numbers=[]

total_sum = 0
for i in range(1, 10000):
    if i in amicable_numbers:
        continue
    else:
        d = sum_factors(find_factors(i))
        if i == sum_factors(find_factors(d)) and i != d:
            amicable_numbers.append(i)
            amicable_numbers.append(d)
            total_sum += i + d
print(total_sum)
