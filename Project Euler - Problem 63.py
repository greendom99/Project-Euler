import math

result = 0
number = 0
n = 1

while number < 10:
    number = math.ceil(10 ** ((n-1)/n))
    result += 10 - number
    n = n+1
print(result)
