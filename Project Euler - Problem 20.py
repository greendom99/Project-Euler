number = 100


def factorial(N):
    product = 1
    for n in range(1, N+1):
        product = product * n
    return product


sum_digits = 0
for letter in str(factorial(number)):
    sum_digits += int(letter)

print(sum_digits)