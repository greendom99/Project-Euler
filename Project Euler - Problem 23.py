import math

number = 220


def find_factors(num):
    factors = []
    if num != 1:
        factors = [1]

    for n in range(2, round(math.sqrt(num)) + 1):
        if num % n == 0:
            factors.append(n)
            factors.append(int(num / n))
    factors.sort()
    return list(set(factors))


def sum_factors(factors):
    sum_fact = 0
    for fact in factors:
        sum_fact += fact
    return sum_fact


abundant_numbers = []

list_numbers = [0]*(2*28123)


for i in range(1, 28123+1):
    list_numbers[i-1] = i
    if i < sum_factors(find_factors(i)):
        abundant_numbers.append(i)

for j in abundant_numbers:
    for k in abundant_numbers:
        list_numbers[j+k-1] = 0

sum_total = 0
for number in list_numbers:
    if number != 0:
        sum_total += number
print(sum_total)
