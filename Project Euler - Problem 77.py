import math

def check_prime(n):
    if n < 2:
        return False
    for j in range(2, round(math.sqrt(n))+1):
        if n % j == 0:
            return False
    return True


target = 1000
list_primes = []
for k in range(1, target+1):
    if check_prime(k):
        list_primes.append(k)

calc_list = [0]*(target+1)
calc_list[0] = 1

# dynamic programming, adaptation of Problem 31
def search():
    for prime in list_primes:
        for i in range(0, len(calc_list)):
            if i - prime >= 0:
                calc_list[i] += calc_list[i-prime]
    return calc_list


answer = next(x[0] for x in enumerate(search()) if x[1] > 5000)
print(answer)
