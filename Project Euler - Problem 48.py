series = 0
for i in range(1, 1001):
    series += i**i

digits = ''
for j in range(0, 10):
    digits = digits + str(series)[-(10-j)]
print(digits)
