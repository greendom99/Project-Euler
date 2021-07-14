def factorial(number):
    product = 1
    for integer in range(1, number + 1):
        product = product * integer
    return product


def sum_factorial_digits(number):
    sum_factorial = 0
    for i in str(number):
        sum_factorial += factorial(int(i))
    return sum_factorial

# dont count 1! = 1 and 2! = 2
answer = -3
for n in range(1, 100000):
    if sum_factorial_digits(n) == n:
        answer += n
print(answer)
